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
result_film_in_category_case_insensitive = expected['film_in_category_case_insensitive']
result_film_cast = expected['film_cast']
result_film_title_case_insensitive = expected['client_from_city']


@pytest.mark.parametrize("category,result", result_film_in_category)
def test_film_in_category(category:Union[int,str], result):
    if result is None:
        assert main.film_in_category(category) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.film_in_category(category))
    else:
        test =  main.film_in_category(category)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.film_in_category(category))

@pytest.mark.parametrize("category,result", result_film_in_category_case_insensitive)
def test_film_in_category_case_insensitive(category:Union[int,str], result):
    if result is None:
        assert main.film_in_category_case_insensitive(category) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.film_in_category_case_insensitive(category))
    else:
        test =  main.film_in_category_case_insensitive(category)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.film_in_category_case_insensitive(category))

@pytest.mark.parametrize("title,result", result_film_cast)
def test_film_cast(title:str, result):
    if result is None:
        assert main.film_cast(title) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.film_cast(title))
    else:
        test =  main.film_cast(title)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.film_cast(title))

@pytest.mark.parametrize("words,result", result_film_title_case_insensitive)
def test_film_title_case_insensitive(words:list, result):
    if result is None:
        assert main.film_title_case_insensitive(words) is None, 'Spodziewany wynik: {0}, aktualny {1}. Błedy wejścia.'.format(result, main.film_title_case_insensitive(words))
    else:
        test =  main.film_title_case_insensitive(words)
        pd.testing.assert_frame_equal(result,test), 'Spodziewany wynik: {0}, aktualny {1}. Błędy implementacji.'.format(result, main.film_title_case_insensitive(words))
