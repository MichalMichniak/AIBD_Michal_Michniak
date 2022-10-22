# -*- coding: utf-8 -*-

import pytest
import main
import pickle
import math
import numpy as np
import pandas as pd

from typing import Union, List, Tuple

expected = pickle.load(open('expected','rb'))

result_film_in_category = expected['film_in_category']
result_number_films_in_category = expected['number_films_in_category'] 
result_number_film_by_length = expected['number_film_by_length']
result_client_from_city = expected['client_from_city']  
result_avg_amount_by_length = expected['avg_amount_by_length'] 
result_client_by_sum_length =  expected['client_by_sum_length']
result_category_statistic_length = expected['category_statistic_length']

@pytest.mark.parametrize("category_id,result", result_film_in_category)
def test_film_in_category(category_id:int, result):
    if result is None:
        assert main.film_in_category(category_id) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.film_in_category(category_id))
    else:
        test =  main.film_in_category(category_id)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.film_in_category(category_id))

@pytest.mark.parametrize("category_id,result", result_number_films_in_category)
def test_number_films_in_category(category_id:int, result):
    if result is None:
        assert main.number_films_in_category(category_id) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.number_films_in_category(category_id))
    else:
        test =  main.number_films_in_category(category_id)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.number_films_in_category(category_id))

@pytest.mark.parametrize("min_length,max_length,result", result_number_film_by_length)
def test_number_film_by_length(min_length: Union[int,float], max_length: Union[int,float], result):
    if result is None:
        assert main.number_film_by_length(min_length,max_length) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.number_film_by_length(min_length,max_length))
    else:
        test =  main.number_film_by_length(min_length,max_length)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.number_film_by_length(min_length,max_length))

@pytest.mark.parametrize("city,result", result_client_from_city)
def test_client_from_city(city:str, result):
    if result is None:
        assert main.client_from_city(city) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.client_from_city(city))
    else:
        test =  main.client_from_city(city)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.client_from_city(city))

@pytest.mark.parametrize("length,result", result_avg_amount_by_length)
def test_avg_amount_by_length(length:Union[int,float], result):
    if result is None:
        assert main.avg_amount_by_length(length) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.avg_amount_by_length(length))
    else:
        test =  main.avg_amount_by_length(length)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.avg_amount_by_length(length))

@pytest.mark.parametrize("sum_min,result", result_client_by_sum_length)
def test_client_by_sum_length(sum_min:Union[int,float], result):
    if result is None:
        assert main.client_by_sum_length(sum_min) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.client_by_sum_length(sum_min))
    else:
        test =  main.client_by_sum_length(sum_min)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.client_by_sum_length(sum_min))

@pytest.mark.parametrize("name,result", result_category_statistic_length)
def test_category_statistic_length(name:Union[int,float], result):
    if result is None:
        assert main.category_statistic_length(name) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.category_statistic_length(name))
    else:
        test =  main.category_statistic_length(name)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.category_statistic_length(name))
