import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego id kategorii.
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    try:
        int(category_id)
    except:
        return None
    strr = f"""
    SELECT
        film.title,language.name as languge,category.name as category
    FROM category
    FULL JOIN film_category ON category.category_id = film_category.category_id
    FULL JOIN film ON film.film_id = film_category.film_id
    FULL JOIN language ON language.language_id = film.language_id
    WHERE category.category_id in ({category_id})
    """
    df = pd.read_sql(strr, con=connection)
    if len(df) == 0:
        return None
    return df
    
def number_films_in_category(category_id:int)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów w zadanej kategori przez id kategorii.
    Przykład wynikowej tabeli:
    |   |category   |count|
    |0	|Action 	|64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    category_id (int): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    try:
        int(category_id)
    except:
        return None
    strr = f"""
    SELECT
        category.name AS category,
        COUNT(film.film_id)
    FROM
        category
    RIGHT JOIN film_category ON film_category.category_id = category.category_id
    RIGHT JOIN film ON film.film_id = film_category.film_id
    WHERE
        category.category_id = {category_id}
    GROUP BY
        category.name;
    """
    df = pd.read_sql(strr, con=connection)
    if len(df) == 0:
        return None
    return df

def number_film_by_length(min_length: Union[int,float] = 0, max_length: Union[int,float] = 1e6 ) :
    ''' Funkcja zwracająca wynik zapytania do bazy o ilość filmów o dla poszczegulnych długości pomiędzy wartościami min_length a max_length.
    Przykład wynikowej tabeli:
    |   |length     |count|
    |0	|46 	    |64	  | 
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    min_length (int,float): wartość minimalnej długości filmu
    max_length (int,float): wartość maksymalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    try:
        int(min_length)
        int(max_length)
    except:
        return None
    strr = f"""
    SELECT
        length,
        COUNT(film_id)
    FROM
        film
    GROUP BY
        length
    HAVING
        film.length >= {min_length} AND film.length <= {max_length}
    """
    df = pd.read_sql(strr, con=connection)
    if len(df) == 0:
        return None
    return df

def client_from_city(city:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o listę klientów z zadanego miasta przez wartość city.
    Przykład wynikowej tabeli:
    |   |city	    |first_name	|last_name
    |0	|Athenai	|Linda	    |Williams
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    city (str): nazwa miaste dla którego mamy sporządzić listę klientów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (type(city) is str) and not (city == ""):
        return None

    strr = f"""
    SELECT
        city,customer.first_name,customer.last_name
    FROM
        city
    INNER JOIN address ON city.city_id = address.city_id 
    INNER JOIN customer ON address.address_id = customer.address_id
    WHERE city IN ('{city}')
    ORDER BY
        customer.last_name ASC,
        customer.first_name ASC
    """
    
    
    df = pd.read_sql(strr, con=connection)
    # if len(df) == 0:
    #     return None
    return df

def avg_amount_by_length(length:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o średnią wartość wypożyczenia filmów dla zadanej długości length.
    Przykład wynikowej tabeli:
    |   |length |avg
    |0	|48	    |4.295389
    
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    length (int,float): długość filmu dla którego mamy pożyczyć średnią wartość wypożyczonych filmów
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(length,int) or isinstance(length,int)):
        return None
    strr = f"""
    SELECT
        length,AVG(payment.amount)
    FROM
        film,inventory,rental,payment
    WHERE film.film_id = inventory.film_id AND inventory.inventory_id = rental.inventory_id AND rental.rental_id = payment.rental_id
    GROUP BY
        length
    HAVING
        length = {length}
    """
    df = pd.read_sql(strr, con=connection)
    # if len(df) == 0:
    #     return None
    return df

def client_by_sum_length(sum_min:Union[int,float])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o sumaryczny czas wypożyczonych filmów przez klientów powyżej zadanej wartości .
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |sum
    |0  |Brian	    |Wyman  	|1265
    
    Tabela wynikowa powinna być posortowane według sumy, imienia i nazwiska klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    sum_min (int,float): minimalna wartość sumy długości wypożyczonych filmów którą musi spełniać klient
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(sum_min,int) or isinstance(sum_min,int)):
        return None
    strr = f"""
    SELECT
        customer.first_name,customer.last_name, SUM(film.length)
    FROM
        rental,customer,film,inventory
    WHERE rental.customer_id = customer.customer_id
        AND inventory.inventory_id = rental.inventory_id
        AND film.film_id = inventory.film_id
    
    GROUP BY
        customer.customer_id
    HAVING
        SUM(film.length) >= {sum_min}
    ORDER BY
        SUM(film.length) ASC,
        customer.last_name ASC,
        customer.first_name ASC
    """
    df = pd.read_sql(strr, con=connection)
    # if len(df) == 0:
    #     return None
    return df

def category_statistic_length(name:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o statystykę długości filmów w kategorii o zadanej nazwie.
    Przykład wynikowej tabeli:
    |   |category   |avg    |sum    |min    |max
    |0	|Action 	|111.60 |7143   |47 	|185
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    name (str): Nazwa kategorii dla której ma zostać wypisana statystyka
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if not (isinstance(name,str)):
        return None
    strr = f"""
    SELECT
        category.name AS category, AVG(film.length), SUM(film.length), MIN(film.length), MAX(film.length)
    FROM
        category,film_category,film
    WHERE
        category.category_id = film_category.category_id
        AND film_category.film_id = film.film_id
    GROUP BY
        category.name
    HAVING
        category.name = '{name}'
    """
    df = pd.read_sql(strr, con=connection)
    return df