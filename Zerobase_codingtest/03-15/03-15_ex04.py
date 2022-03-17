# 1
import math

def solution(arr):
  
   arr.remove(max(arr))
   arr.remove(min(arr))
    
   return int(sum(arr) / len(arr))
  
 # 2
import statistics

def solution(arr):

  arr.remove(max(arr))
  arr.remove(min(arr))

  return int(statistics.mean(arr))
