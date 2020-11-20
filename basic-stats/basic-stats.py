#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is a module with no inputs
def mean(x):   # This is the definition in the head.
    sum=0
    count=0
    sd1=0
    import math
    for i in x:
        count+=1
    for i in x:
        sum += i
    m=sum/(count)
    for i in x:
        sd1 += (i-m)**2
    sd2 = sd1/count
    sigma = math.sqrt(sd2)
    return m, sigma

def stdev(x):   # This is the definition in the head.
    sd1=0
    for i in x:
        sd1 += (i-m)**2
    sd2 = sd1/count
    sigma = math.sqrt(sd2)
    return sigma
