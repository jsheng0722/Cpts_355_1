# CptS 355 - Fall 2020 - Assignment 3
# Please include your name and the names of the students with whom you discussed any of the problems in this homework

debugging = True
def debug(*s): 
     if debugging: 
          print(*s)

## problem 1-a) getNumCases - 10%
def getNumCases(data,counties,months):
     number = 0                                                                 # initial number
     for k, v in data.items():                                                  # in data. there are k and v as {k:v}
          if k in counties:                                                     # if k in countries list
               for key, value in v.items():                                     # search in its value v = {key:value}
                    for i in months:                                            # if i in month list
                         if i in key:                                           # search in key
                              number += value                                   # get the sum number
     return number                                                              # return number

## problem 1-b) getMonthlyCases - 15%
def getMonthlyCases(data):
     dic = {}
     for k, v in data.items():                                                  # k, v in data items
          for key, value in v.items():                                          # key, value in data items
               dic[key] = dic.get(key,{})                                       # create dict with empty value
     for i in dic.keys():                                                       # for each dict key
          for k, v in data.items():                                             # search in data
               if i in data[k]:                                                 # if i which is month in data[k]
                    dic[i][k] = data[k][i]                                      # get value from data and put in dict
     return dic                                                                 # return dic dict

from functools import reduce
## problem 1-c) mostCases - 15%
def mostCases(data):
     dic = getMonthlyCases(data)                                                # get the info from getMonthlyCases function
     list1 = list(dic.keys())                                                   # create list get each months in order
     list2 = list(map(lambda x:sum(x.values()),list(dic.values())))             # get the sum of data in each months
     dic_z = dict(zip(list1,list2))                                             # zip them
     result = reduce(lambda x, y: x if x > y else y,dic_z.values())             # get the largest data
     return list1[list(dic_z.values()).index(result)],result                    # return the largest data and its month


## problem 2a) searchDicts(L,k) - 5%
def searchDicts(L,k):
     for index in reversed(L):                                                  # search from back of L, so it need reverse
          if k in index:                                                        # if k in it
               return index[k]                                                  # found it and return its value
     return None                                                                # if cant find, return None

## problem 2b) searchDicts2(L,k) - 10%
def searchDicts2(L,k):
    return searchHelper(L, k, L[-1][0])                                         # search from the last index

def searchHelper(L,k,index):                                                    # searchDicts2 help function
    if k in L[index][1]:                                                        # if in the index dic
        return L[index][1][k]                                                   # return its value
    elif index == 0:                                                            # else if index is 0
        return None                                                             # cant't find and return None
    else:                                                                       # otherwise
        return searchHelper(L,k,L[index][0])                                    # go to specific index

## problem 3 - adduptoZero - 10%
from itertools import combinations
def adduptoZero(L,n):
     list1 = list(combinations(L,n))                                            # use combinations to get sublists
     list2 = []                                                                 # prepare empty list list2
     for i in list1:                                                            # for each sublists in list1
          if sum(i) == 0:                                                       # if the sum of elements in sublists is 0
               list2.append(list(i))                                            # put it in list2
     return sorted(list2)                                                       # return sorted list2

## problem 4 - getLongest - 10%
def getLongest (L):
     dic = {}                                                                   # for every new call
     def getLongestHelper(L):                                                   # helper function for recursion
          nonlocal dic                                                          # nonlocal to construct dic
          for i in L:                                                           # for elements in L
               if type(i) is str:                                               # if it's string
                    dic[i] = len(i)                                             # dic[element] = its length
               else:                                                            # if it's list or other
                    getLongestHelper(i)                                         # get the elements in it with same way
          return dic                                                            # helper function finally construct a dic
     getLongestHelper(L)                                                        # call helper function in main function
     return list(dic.keys())[list(dic.values()).index(max(dic.values()))]       # return the longest string

## problem 5 - apply2nextN - 20%
class apply2nextN (object):
     def __init__(self, f, n, L):                                               # initialize
          self.op = f                                                           # op for lambda
          self.Li = list(L)                                                     # make sure Li is list
          self.index = 0                                                        # for go next
          self.Li1 = [self.Li[i:i + n] for i in range(0, len(self.Li), n)]      # get the sublists with n length

     def __next__(self):
          try:
               self.current = reduce(self.op,(self.Li1[self.index]))            # get current Li1 and use combining function
               self.index = self.index + 1                                      # way to go next
               return self.current                                              # if success, return self.current
          except:
               raise StopIteration                                              # throw when out of the range

     def __iter__(self):
          return self

