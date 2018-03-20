# -*- coding: utf-8 -*-
import xlrd
import sys
import chardet
from xlutils.copy import copy
import os  
import json
import xlwt
import sys

list_finished = [];
def get_json_file(filename):
    f = open(filename)  #设置以utf-8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
    setting = json.load(f)
    return setting

def transform():
	for idx, val in enumerate(list_map['options1']):
		code = val
		name_bank = list_map['optionsValue1'][idx]
		st_ = '<option value="'+code+'">' + name_bank + '</option>'
		# print('code...',code)
		# print('name_bank...',name_bank)
		# print('index...',idx)
		# print('all...',st_)
		list_finished.append(st_)

def write():
	with open("test.txt","w") as f:
		for item in list_finished:
			f.write(item)
			f.write('\n')
			
list_map = get_json_file('test.json')
transform()
write()
