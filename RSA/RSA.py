#coding:utf-8
#Author:Joe1sn
#python 3.8.2
from random import randint

global is_ch
is_ch = 0
def ErrorCather(zh_msg,en_msg):
	if is_ch: print(zh_msg)
	else: print(en_msg)


class RSA(object):
	"""
	docstring for RSA
	"""
	def __init__(self, KeyLen=1024):
		self.ChineseMod = False
		self.Debug = True

		self.n = 0
		self.e = 65537
		self.p = 0
		self.q = 0
		self.phi_n = 0

		# RSA.test()
		#1.初始化生成p,q
		#pq不相等，二进制共模数长度和KeyLen一致
		while (self.p==self.q and bin(self.p*self.q) != KeyLen+2):
			self.p = RSA.PrimerGen(KeyLen//2)
			self.q = RSA.PrimerGen(KeyLen//2)
		
		#2.得到n和phi(n),求逆得到u
		self.n = self.p*self.q
		self.phi_n = (self.p-1)*(self.q-1)
		#3.利用欧几里得拓展求私钥d
		# self.d = RSA.ExtendEuclid(self.e,self.phi_n)
		ed = 1
		while 1:
			#虽然我知道这里利用拓展欧几里得算法可以求逆
			#但是结果可能为负数，而且速度跟不上
			#而且公钥e就是一个素数，通过遍历很快就能找到
			if (ed*self.phi_n+1)%self.e==0:
				self.d = (ed*self.phi_n+1)//self.e
				break
			ed+=1

		if self.Debug:
			print("p>",self.p)
			print("q>",self.q)
			print("n>",self.n)
			print("phi_n>",self.phi_n)
			print("e>",self.e)
			print("d>",self.d)

	#bytes 转 hex
	#str->byte->number
	def Byte2Hex(Msg):
		return int.from_bytes((bytes(Msg,encoding='utf8')),byteorder='big',signed=False)

	#number->byte->str
	def Hex2Byte(num):
		num = hex(num)[2:]#去掉十六进制的0x开头
		result = ""
		i = 0
		while(i<len(num)):#两两一组解析为十六进制数
			result+=chr(int(num[i]+num[i+1],16))
			i+=2
		return result

	#报错输出
	def ErrorCather(self,ErrorMsg_zhCN, ErrorMsg_en):
		if self.ChineseMod:
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
				return result
			else:
				ErrorCather("参数必须大于0","arguments must lager than 0")
				return
		else:
			ErrorCather("参数必须全为整数","arguments must be integers")
			return

	#大素数生成
	def PrimerGen(size): #生成size位的素数
		if str(size).isdigit():	#如果size是素数
			while True:
				n = randint(1<<(size-1), 1 << (size+1))	#求2^size之间的大数
														#利用二进制右移得到大数
				if n % 2 != 0:		#排除偶数
					found = True	#设置返回结果

					# 随机性测试
					for i in range(0, 2):	#进行 2*3 轮素性检测
											#这里 2轮,检测函数 3轮
						#如果检测失败
						if RSA.PrimerCheck(n) == False:
							found = False
							break#退出
					#通过检测
					if found == True:
						return n

		else:	#size非素数，报错+返回None
			ErrorCather("参数为素数的位数","argument is digits of a primer number")
			return

	#Miller Rabin素性检测
	#费马小定理+二次探测
	def PrimerCheck(num,times=3): #对num检测times次
		if str(num).isdigit():
			if num < 3:
				return num==2
			u = num-1
			t = 0
			while u%2 ==0:#若为偶数
				u//=2
				t+=1
			for i in range(1,times+1): 	#费马小定理检测
				x = randint(2,num-1)	#生成size位的随机数
				v = RSA.ReModule(x,u,num)
				if v==1 or v==num-1:	#余数为1，则该数可能为素数
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

	#欧几里得算法
	# return (a,b)
	def Ecuild(a,b):
		#判断ab是否为数字
		if a.isdigit() and b.isdigit():
			if a>0 and b>0:					#ab均大于0
				try:						#是的话开始计算

				# 算法简介：
				# 	一般欧几里得算法要求 a<b 否则交换
				# 	这里利用python的语法糖，
				# 	若a>b，那么第一个循环的过程是交换a,b
				# 	而且利用循环避免重复递归导致递归深度过大超过语言规定最大深度

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
					#2-3 更新R S T和R' S' T'
					R, _R = _R, tempR
					S, _S = _S, tempS
					T, _T = _T, tempT
				#3.循环完毕，返回
				return T
			#中途出错
			except TypeError as e:
				ErrorCather("类型错误",e)

	#欧拉定理求公钥
	def Euler(a,n): #a^phi(n)−1
		if a%n==0:
			print(str(a)+"%"+str(n)+"==0")
			return False
		phi_n = 0	#使用该变量来遍历
		for i in range(1,n):
			if RSA.gcd(i,n)!=0:
				phi_n+=1
		return pow(a,phi_n)-1

	#0x50字节对齐
	def ByteAlign(self,Msg):
		# 如果不满0x100对齐，就补上\x00
		if (0x50-len(Msg)%0x50) != 0:
			rest = (0x50-len(Msg)%0x50)
			Msg += "\x00"*rest
		return Msg

	#对齐检查
	def AlignCheck(Msg):
		if len(Msg)%0x50 != 0:
			ErrorCather("参数未对齐","arguments must aligned to 0x100")
			return 0
		else:
			return 1

	#RSA加密模块
	def Encrypt(self,Msg):
		#检查对齐
		if len(Msg) != 0x50:
			ErrorCather("消息长度必须为0x50","Message length must be 0x50")
			return
		else:
			cipher = RSA.ReModule(RSA.Byte2Hex(Msg),self.e,self.n)
			return cipher

	#RSA解密模块
	def Decrypt(self,Cipher):
		return RSA.Hex2Byte((RSA.ReModule(Cipher,self.d,self.n)))