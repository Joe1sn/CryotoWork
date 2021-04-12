#coding:utf-8
#Author:Joe1sn
#python 3.8.2

ChineseMod = 1 #报错显示是否为中文

#报错输出
def ErrorCather(ErrorMsg_zhCN, ErrorMsg_en):
	if ChineseMod:
		print(ErrorMsg_zhCN)
	else:
		print(ErrorMsg_en)

#欧几里得实现
def Eucild(a,b):
	#判断ab是否为数字
	if str(a).isdigit() and str(b).isdigit():
		if a>0 and b>0:					#ab均大于0
			try:						#是的话开始计算
			#算法简介：
			#	一般欧几里得算法要求 a<b 否则交换
			#	这里利用python的语法糖，
			#	若a>b，那么第一个循环的过程是交换a,b
			#	而且利用循环避免重复递归导致递归深度过大超过语言规定的最大递归深度
				while a != 0:			
					a, b = b % a, a
				return b
			#循环报错
			except (TypeError, ValueError):
				ErrorCather("循环失败","loop error")
		else:
			ErrorCather("两参数必须为大于零整数","two arguments must be unsigned integers")
	else:
		ErrorCather("两参数必须为大于零整数，而不是其他","two arguments must be unsigned integers,arguments type error")