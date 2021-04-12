#coding:utf-8
#Author:Joe1sn
#python 3.8.2

from random import randint #随机数生成库

ChineseMod = 0

#报错输出
def ErrorCather(ErrorMsg_zhCN, ErrorMsg_en):
	if ChineseMod:
		print(ErrorMsg_zhCN)#输出中文
	else:
		print(ErrorMsg_en)#输出英文

#模重复平方
def ReModule(b,n,m): #b^n(mod m)
	#参数为数字
	if str(b).isdigit() and str(n).isdigit() and str(m).isdigit():
		#参数必须大于0
		if b > 0 and n>0 and m>0:
			#二进制转换n
			result=1	#返回值
			n1=bin(n)	#幂数转为二进制
			BinList = list(str(n1)[2:][::-1]) #二进制反序
			#开始遍历
			for i in BinList:	#模重复平方
				# print(result)
				if int(i) == 1:
					result = (result*b)%m
					b = (b*b)%m
				else:
					b = (b*b)%m

			return result

		else:
			ErrorCather("参数必须大于0","arguments must lager than 0")
			return
	else:
		ErrorCather("参数必须全为整数","arguments must be integers")
		return

#费马素性检测
def Fermat(number):
	#1.再合适范围内选择一个随机数
	a = randint(2,number-2)
	r = ReModule(a,number-1,number)
	if r != 1:
		return False
	else:
		return True