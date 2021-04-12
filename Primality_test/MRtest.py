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