# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 10:19:09 2017

@author: ADITYA.SHETTY
"""
import codecs

with codecs.open('C:/Users/Aditya.Shetty/.spyder-py3/projects/Examples/samples/a.txt', 'r') as f:
    content = f.read()
    f.close()

print(content)
