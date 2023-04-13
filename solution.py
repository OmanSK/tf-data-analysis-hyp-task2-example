import pandas as pd
import numpy as np
from scipy.stats import ks_2samp


chat_id = 143893840 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = 0.07
    result = ks_2samp(x, y)
    
    return result.pvalue < p_value
