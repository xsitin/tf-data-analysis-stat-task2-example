import pandas as pd
import numpy as np

from scipy.stats import uniform


chat_id = 385459798 # Ваш chat ID, не меняйте название переменной

def confidence_interval(confidence_level, p_values):
    maximum_likelihood = np.max(p_values)
    alpha = 1 - confidence_level
    loc,scale = uniform.fit(p_values)
    quantile = uniform.ppf(1 - alpha, loc=loc, scale=scale)
    right_bound = maximum_likelihood + (quantile - maximum_likelihood)
    return [right_bound, maximum_likelihood]


def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return confidence_interval(p, x)
