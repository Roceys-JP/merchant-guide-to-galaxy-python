#coding:utf-8
from Roma_to_num_test import *
'''

'''
Romanarray=['I','V','X','L','C','D','M']
#print Romanarray

input_line ='glob glob Silver is 34 Credits'

word_dic = {}#以字典来对应单词和罗马数字
coin_dic = {}#以字典来对应货币和价值
if input_line[-1] in Romanarray:
    input_line_array = input_line.split(' ')#以空格截取
    word_dic[input_line_array[0]] = input_line_array[2]#取第一个和最后一个元素
    print word_dic

if input_line[-1] <> 'Credits':
    input_line_array = input_line.split(' ')#以空格截取
    print int(input_line_array[-2])
    print input_line_array[-3]
    coin_dic[input_line_array[-3]] = int(input_line_array[-2])
