#coding:utf-8
#Author:Joe1sn
#python 3.8.2
from random import randint

ChineseMod = 1 #报错显示是否为中文

#报错输出
def ErrorCather(ErrorMsg_zhCN, ErrorMsg_en):
	if ChineseMod:
		print(ErrorMsg_zhCN)
	else:
		print(ErrorMsg_en)

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

def MillerRabin(num,times=3): #对num检测times次
	if str(num).isdigit():
		if num < 3:				#若输入<3
			return num==2
		u = num-1
		t = 0
		while u%2 ==0:#若为偶数
			u//=2
			t+=1
		for i in range(1,times+1): 	#费马小定理检测
			x = randint(2,num-1)	#生成size位的随机数
			v = ReModule(x,u,num)
			if v==1 or v==num-1:	#余数为正负1，则该数可能为素数
				continue
			for j in range(t+1):
				v = v*v%num
				if v==num-1:
					break
			else:
				return False
		return True
	else:
		ErrorCather("参数必须全为整数","arguments must be integers")
