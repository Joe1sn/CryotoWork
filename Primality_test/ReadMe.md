# Fermat测试

## 基本原理

**费马定理**

> 若$n$是素数，且$a$是任何满足$1 \leq a \leq n-1$的整数，则
>
> ​					$a^{n-1}\equiv1 \ mod \ n$

由此可得：

要判定素性数n，若能在区间内找到一个整数$a$使得$a^{n-1} \neq 1 \ mod \ n$，则 $n$ 为一个和数

## 代码

**源代码**

```python
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
    #2.根据费马定理判断
	r = ReModule(a,number-1,number)
	if r != 1:
		return False
	else:
		return True
```

**测试代码**

```python
import Fermat
from tqdm import tqdm

trueTime = 0	#函数返回正确的次数
falseTime = 0	#函数返回错误的次数

#被测试数M，是个质数
M = 26093293871252647379645877975828560475572123676376044555600092424771100007425342027189289292730506092675260705227850490901691304063378764564153221430645537

#被测试数N，是个合数
N = M+1
for i in tqdm(range(100000), ncols=120):	#尽心100000次循环测试
	if Fermat.Fermat(M):
		trueTime += 1
	else:
		falseTime += 1

print("TrueTime",trueTime)
print("FlaseTime",falseTime)
print()

#清空次数并统计
trueTime = 0
falseTime = 0

for i in tqdm(range(100000), ncols=120):	#尽心100000次循环测试
	if Fermat.Fermat(N):
		trueTime += 1
	else:
		falseTime += 1

print("TrueTime",trueTime)
print("FlaseTime",falseTime)
```

**测试结果**

![FermatTest](..\img\Primality_test\FermatTest.png)

# MillerRabin测试

## 基本原理

> 由上面的Fermat的基础可知：由于$n$是奇数，则$n-1$为偶数，设$2t = n-1$，$a^{n-1}=(a^t)^2$，如果$a^t = \pm 1 \ mod \ n$，那么$n$就是一个素数了，就没有必要再继续计算下去了

## 代码

**源代码**

```python
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
```

**测试代码**

```python
import MillerRabin
from tqdm import tqdm

trueTime = 0	#函数返回正确的次数
falseTime = 0	#函数返回错误的次数

#被测试数M，是个质数
M = 26093293871252647379645877975828560475572123676376044555600092424771100007425342027189289292730506092675260705227850490901691304063378764564153221430645537

#被测试数N，是个合数
N = M+1
for i in tqdm(range(100000), ncols=120):	#尽心100000次循环测试
	if MillerRabin.MillerRabin(M):
		trueTime += 1
	else:
		falseTime += 1

print("TrueTime",trueTime)
print("FlaseTime",falseTime)
print()

#清空次数并统计
trueTime = 0
falseTime = 0

for i in tqdm(range(100000), ncols=120):	#尽心100000次循环测试
	if MillerRabin.MillerRabin(N):
		trueTime += 1
	else:
		falseTime += 1

print("TrueTime",trueTime)
print("FlaseTime",falseTime)
```

**测试结果**

![MillerRabinTest](..\img\Primality_test\MillerRabinTest.png)