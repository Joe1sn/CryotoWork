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
			return R,S,T
		#中途出错
		except TypeError as e:
			ErrorCather("类型错误",e)

#利用改算法求逆
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
			if r_p != 1:
				ErrorCather("无法求得逆 "+str(r_p),"No inverse value can be computed" + str(r_p))
				return
			while s_p < 0:
				s_p += modulus
			value = s_p
		except Exception as e:
			raise e
