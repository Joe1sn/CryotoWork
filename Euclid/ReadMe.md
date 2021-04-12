# 简介

> 欧几里得算法又称**辗转相除法**，是指用于计算两个**非负整数**a，b的**最大公约数**。应用领域有数学和计算机两个方面。计算公式 $gcd(a,b) = gcd(b,a mod b)$

# python实现

主程序

```python
#coding:utf-8
#Author:Joe1sn
#python 3.8.2

ChineseMod = 1 #报错显示是否为中文

#欧几里得实现
def Ecuild(a,b):
	#判断ab是否为数字
	if a.isdigit() AND b.isdigit():
		if a>0 and b>0:					#ab均大于0
			try:						#是的话开始计算
			'''
			算法简介：
				一般欧几里得算法要求 a<b 否则交换
				这里利用python的语法糖，
				若a>b，那么第一个循环的过程是交换a,b
				而且利用循环避免重复递归导致递归深度过大，语言报错
			'''
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

#报错输出
def ErrorCather(ErrorMsg_zhCN, ErrorMsg_en):
	if ChineseMod:
		print(ErrorMsg_zhCN)
	else:
		print(ErrorMsg_en)
```

测试程序：

```python
from Eucild import Eucild

print(Eucild(120,3))
print(Eucild(3,120))
print(Eucild(0,0))
print(Eucild(-2,-3))
print(Eucild("hello","world"))
```

输出

![result](..\img\Euclid\result.png)
