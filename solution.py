import pandas as pd
import numpy as np
from scipy.stats import ks_2samp, ttest_ind
from statsmodels.stats.weightstats import ztest as z_test


chat_id = 143893840 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    p_value = 0.07
    result_1 = ks_2samp(x, y)
    result_2 = ttest_ind(x, y, equal_var=False)
    result_3 = z_test(x, y)
    
    result_1 = result_1.pvalue
    result_2 = result_2.pvalue
    result_3 = result_3[-1]
    
    
    return min([result_1, result_2, result_3]) < p_value
