import math
import os
import random
import re
import sys



# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    new_arr = arr.copy()
    arr_for_min = arr.copy()

    maxs = []
    mins = []
    for i in range(1, 5):
        min_ = min(arr_for_min)
        try:
            min_ = min(arr_for_min)
            arr_for_min.remove(min_)
            mins.append(min_)
            
        except:
            break

    for i in range(1, 5):    
        try:
            max_ = max(new_arr)
            new_arr.remove(max_)
            maxs.append(max_)
        except:
            break

    x= sum(mins)
    y = sum(maxs)
    print(f"{x} {y}")
if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)