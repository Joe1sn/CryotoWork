# 欧几里得拓展

> **扩展欧几里得算法**是欧几里得算法（又叫辗转相除法）的扩展。除了计算a、b两个整数的**最大公约数**，此算法还能找到整数x、y（其中一个很可能是负数）。通常谈到最大公因子时, 我们都会提到一个非常基本的事实: **给予二整数 a 与 b, 必存在有整数 x 与 y 使得ax + by = gcd(a,b)**。有两个数a,b，对它们进行辗转相除法，可得它们的最大公约数——这是众所周知的。然后，收集辗转相除法中产生的式子，倒回去，可以**得到ax+by=gcd(a,b)的整数解**

# 算法实现原理

**以求  $104s+25t = gcd(104,25)$ 中的s、t为例子**

$104 = 25 \times 4 +4 $

$25 = 4 \times 6 + 1$

$4 = 4 \times 1 +0$

那么反过来就是

$1 = 25 - 4 \times 6$

$1= 25-6\times(104-25\times4)$

$1=25\times25-104\times6$

**式子每一轮变为 $a s_n +b t_n = gcd(a,b)$**

对$j = 0,1,2,3...$有以下推导关系

$s_{-2} = 1$  $s_{-1}=0$  $s_{j}=s_{j-2}-q_j s_{j-1}$

$t_{-2}=0$   $t_{-1} = 1$  $t_j = t_{j-2}-q_jt_{j-1}$          $j=0,1,2,3...b-1,n$

$q_j=[r_{j-2}/r_{j-1}]$

| q     | R     | R'        | S         | S'    | T         | T'    |
| ----- | ----- | --------- | --------- | ----- | --------- | ----- |
| $q_j$ | $r_j$ | $r_{j+1}$ | $s_{j-1}$ | $s_j$ | $t_{j-1}$ | $t_j$ |

最后将推导过程变为以下表格

| R' != 0 ? | q    | R     | R'   | S    | S'   | T    | T'   |
| --------- | ---- | ----- | ---- | ---- | ---- | ---- | ---- |
|           |      | a=104 | b=25 | 1    | 0    | 0    | 1    |
| True      | 4    | 25    | 4    | 0    | 1    | 1    | -4   |
| True      | 6    | 4     | 1    | 1    | -6   | -4   | 25   |
| True      | 4    | 1     | 0    | -6   | 25   | 25   | -104 |
| **False** |      |       |      |      |      |      |      |

# python实现

主程序

```python
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

#拓展欧几里得实现
def ExtendEuclid(a,b):

	#检查参数
	if (not str(a).isdigit()) or (not str(b).isdigit()):
		ErrorCather("参数为大于0的整数","argument must be integers greater than 0")
		return
	a,b = int(a),int(b)

	if a <=0 or b <=0:
		ErrorCather("参数为大于0的整数","argument must be integers greater than 0")
		return
	else:
		#如果 a< b，交换ab的值
		if a < b:
			a,b = b,a
		try:
			#进行循环的计算
			#	1赋初始值
			R,S,T = a,1,0
			_R,_S,_T = b,0,1

			#	2开始循环
			while _R != 0:

				q = R // _R #2-1 得到整商

				#2-2 获得暂时的R' S' T'
				tempR = R-q*_R
				tempS = S-q*_S
				tempT = T-q*_T

				#2-3 更新R S T
				R = _R
				S = _S
				T = _T

				#2-4 更新R' S' T'
				_R = tempR
				_S = tempS
				_T = tempT

			#3.循环完毕，返回
			return R,S,T

		#中途出错
		except TypeError as e:
			ErrorCather("类型错误",e)
```

测试

```python
from ExtendEuclid import ExtendEuclid
print(ExtendEuclid(104,25))
print(ExtendEuclid(25,104))
print(ExtendEuclid("a","b"))
```

测试结果

![result](..\img\Extend_Euclid\result.png)

# 拓展欧几里得在求逆中的应用

> 假设$b<m$，当$(m,b)=1$时，$sm+tb=(m,b) = 1$，则 $tb = 1(mod m)$。
>
> 称 t为b的逆元

```python
def Inverse(value,modulus):
		modulus = int(modulus)#确保模数为数字
		#对模数进行检查
		if modulus == 0:
			ErrorCather("模数不能为0","Modulus cannot be zero")
			return
		if modulus < 0:
			ErrorCather("模数不能为负","Modulus cannot be negative")
			return
		try:
            #开始拓展欧几里得算法
			r_p, r_n = value, modulus
			s_p, s_n = 1, 0
			while r_n > 0:
				q = r_p // r_n
				r_p, r_n = r_n, r_p - q * r_n
				s_p, s_n = s_n, s_p - q * s_n
                
			if r_p != 1:	#不满足互素条件
				ErrorCather("无法求得逆 "+str(r_p),"No inverse value can be computed" + str(r_p))
				return
			while s_p < 0:
				s_p += modulus
			value = s_p
		except Exception as e:
			raise e
```

