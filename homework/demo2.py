
def main():
	Choose = eval(input())
	if Choose == 1:
	    getSwitchC()
	elif Choose == 2:
	    getSwitchF()
	else:
		print("请重新输入：")
		main()


def getSwitchC():
	num = eval(input("你输入的华氏度是："))
	C = round((num-32)/1.8)
	print("转换的摄氏度是：", C,"°C")

def getSwitchF():
	num = eval(input("你输入的摄氏度是："))
	F = round(num*1.8+32)
	print("转换的华氏度是：", F,"°F")


if __name__ == '__main__':
	proto = '''【F -> C】转换摄氏度请输入1,【C -> F】转换华氏度请输入2'''
	print(proto)
	print('你的选择是 1 or 2')
	main()
