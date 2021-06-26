# from DES import *
import DES

print("1.Encrypto")
print("2.Decrypto")
mode = input()

if __name__ == '__main__':
	if mode == '1':
		print("请输入信息输入字符串不能为空：")
		message = input().replace(' ','')
		print("请输入你的秘钥：")
		key = input().replace(' ','')
		s = DES.all_message_encrypt(message,key)
		out_mess = DES.bin2str(s)
		print("加密过后的内容:"+ out_mess)
		DES.write_in_file(out_mess)
	elif mode == '2':
		print("请输入你的秘钥：")
		key = input().replace(' ', '')
		message = DES.read_out_file()
		s = DES.all_message_decrypt(message, key)
		#out_mess = bin2str(s)
		print("解密后的信息："+ s)
	else:
		print("请重新输入！")
