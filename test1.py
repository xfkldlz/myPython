#!/usr/bin/env pythons
# -*- coding: utf-8 -*-
def f(a):
    def g(i):
        for j in range(len(a)):
            if not (i % a[j]):
                return -1
            elif a[j]*a[j] > i:
                return i
        return i
    return g

a = [3, 5, 7]
h = f(a)
b = [i for i in range(a[len(a) - 1] + 2, 100, 2) if h(i) != -1]
a += b
a.insert(0,2)
print(a)
