import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 123456 # Ваш chat ID, не меняйте название переменной

def confidence_interval(confidence_level, p_values):
    n = len(p_values)
    z_critical = norm.ppf(1 - (1 - confidence_level) / 2)
    p_values_sorted = np.sort(p_values)
    lower_p = p_values_sorted[int(np.floor((n - 1) * (1 - confidence_level) / 2))]
    upper_p = p_values_sorted[int(np.ceil((n - 1) * (1 - confidence_level) / 2))]
    lower_b = 0.05
    upper_b = lower_b + (upper_p - lower_p) / z_critical
    return [lower_b, upper_b]

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return confidence_interval(p, x)
