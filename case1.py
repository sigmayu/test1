# -*- coding: utf-8 -*-

"""
@Time    : 2021/7/4 21:02
@Author  : yugang
"""


def list_of_sort(list1:list):
    for i in range(len(list1)-1):
        for j in range(len(list1)-1-i):
            if list1[j]>list1[j+1]:
                list1[j],list1[j+1]=list1[j+1],list1[j]
    return list1
res = list_of_sort([1, 3, 4, 5, 2, -4, 7, -6, 9, -2])
print(res)