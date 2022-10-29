import numpy as np
import pickle

import psycopg2 as pg
import pandas.io.sql as psql
import pandas as pd

from typing import Union, List, Tuple

connection = pg.connect(host='pgsql-196447.vipserv.org', port=5432, dbname='wbauer_adb', user='wbauer_adb', password='adb2020');

def film_in_category(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str, dokładnie taki jak podana wartość
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category) == int:
        condition = f" category.category_id = {category}"
    elif type(category) == str:
        condition = f" category.name = '{category}'"
    else:
        return None
    strr = f"""
    SELECT
        film.title,language.name as languge, category.name as category
    FROM category
    INNER JOIN film_category ON category.category_id = film_category.category_id
    INNER JOIN film ON film.film_id = film_category.film_id
    INNER JOIN language ON language.language_id = film.language_id
    WHERE {condition}
    ORDER BY film.title,language.name
    """

    df = pd.read_sql(strr, con=connection)
    return df
    
def film_in_category_case_insensitive(category:Union[int,str])->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuł filmu, język, oraz kategorię dla zadanego:
        - id: jeżeli categry jest int
        - name: jeżeli category jest str
    Przykład wynikowej tabeli:
    |   |title          |languge    |category|
    |0	|Amadeus Holy	|English	|Action|
    
    Tabela wynikowa ma być posortowana po tylule filmu i języku.
    
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
    
    Parameters:
    category (int,str): wartość kategorii po id (jeżeli typ int) lub nazwie (jeżeli typ str)  dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(category) == int:
        condition = f" category.category_id = {category}"
    elif type(category) == str:
        condition = f" category.name ~* '{category}'"
    else:
        return None
    strr = f"""
    SELECT
        film.title,language.name as languge, category.name as category
    FROM category
    INNER JOIN film_category ON category.category_id = film_category.category_id
    INNER JOIN film ON film.film_id = film_category.film_id
    INNER JOIN language ON language.language_id = film.language_id
    WHERE {condition}
    ORDER BY film.title,language.name
    """

    df = pd.read_sql(strr, con=connection)
    return df
    
def film_cast(title:str)->pd.DataFrame:
    ''' Funkcja zwracająca wynik zapytania do bazy o obsadę filmu o dokładnie zadanym tytule.
    Przykład wynikowej tabeli:
    |   |first_name |last_name  |
    |0	|Greg       |Chaplin    | 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.
    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    title (str): wartość id kategorii dla którego wykonujemy zapytanie
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    if type(title) == str:
        condition = f" film.title = '{title}'"
    else:
        return None
    strr = f"""
    SELECT
        actor.first_name,actor.last_name
    FROM film
    INNER JOIN film_actor ON film_actor.film_id = film.film_id
    INNER JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE {condition}
    ORDER BY actor.last_name,actor.first_name
    """

    df = pd.read_sql(strr, con=connection)
    return df
    

def film_title_case_insensitive(words:list) :
    ''' Funkcja zwracająca wynik zapytania do bazy o tytuły filmów zawierających conajmniej jedno z podanych słów z listy words.
    Przykład wynikowej tabeli:
    |   |title              |
    |0	|Crystal Breaking 	| 
    
    Tabela wynikowa ma być posortowana po nazwisku i imieniu klienta.

    Jeżeli warunki wejściowe nie są spełnione to funkcja powinna zwracać wartość None.
        
    Parameters:
    words(list): wartość minimalnej długości filmu
    
    Returns:
    pd.DataFrame: DataFrame zawierający wyniki zapytania
    '''
    for word in words:
        if type(word) == str:
            condition = f" film.title ~~* '%{word}%',"
        else:
            return None
    strr = f"""
    SELECT
        DISTINCT(film.title)
    FROM film
    INNER JOIN film_actor ON film_actor.film_id = film.film_id
    INNER JOIN actor ON film_actor.actor_id = actor.actor_id
    WHERE {condition[:-1]}
    """

    df = pd.read_sql(strr, con=connection)
    return df