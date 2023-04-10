import pandas as pd
import numpy as np


chat_id = 1474426447 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    import scipy.stats as sts
    #x = [[x_cnt,x_success],[y_cnt,y_success]]
    x =  [[x_success,x_cnt-x_success],[y_success,y_cnt-y_success]]
    oddsratio, pvalue = sts.fisher_exact(x)
    #answer = pvalue > 0.04
    answer = pvalue < 0.04
    return answer
   
  
  
  
    #p1 = x_success / x_cnt
    #p2 = y_success / y_cnt
    #p = (x_success + y_success) / (x_cnt + y_cnt)
    #d = p2 - p1
    #se = (p*(1-p)*(1/x_cnt + 1/y_cnt))**0.5
    #z = d / se
    #alpha = 0.04
    #z_critical = sts.norm.ppf(1 - alpha/2)
    #if abs(z) > z_critical:
        #return True # отклоняем нулевую гипотезу
    #else:
        #return False # не отклоняем нулевую гипоте
    #return ... # Ваш ответ, True или False
