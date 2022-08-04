#!/usr/bin/env pythons
# -*- coding: utf-8 -*-

def g(i, a):
    for j in range(len(a)):
        if not(i % a[j]):
            return -1
    return i


a = [3, 5, 7]
b = [i for i in range(a[len(a) - 1] + 2, 100, 2) if g(i, a) != -1]
a += b
a.insert(0,2)
print(a)
