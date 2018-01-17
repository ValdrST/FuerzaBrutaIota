def main():
	f0 = open("contras0.txt", "w")
	f1 = open("contras1.txt", "w")
	f2 = open("contras2.txt", "w")
	f3 = open("contras3.txt", "w")
	f4 = open("contras4.txt", "w")
	f5 = open("contras5.txt", "w")
	f6 = open("contras6.txt", "w")
	f7 = open("contras7.txt", "w")
	f8 = open("contras8.txt", "w")
	f9 = open("contras9.txt", "w")

	for i in range(0,999999):
		if (i<10):
			word = "00000" + str(i)
		elif (i < 100 and i >= 10):
			word = "0000" + str(i)
		elif (i < 1000 and i >= 100):
			word = "000" + str(i)
		elif (i< 10000 and i >= 1000):
			word = "00" + str(i)
		elif (i< 100000 and i >= 10000):
			word = "0" + str(i)
		else:
			word = str(i)
		escribir(word,f1,f2,f3,f4,f5,f6,f7,f8,f9,f0)
	f0.close()
	f1.close()
	f2.close()
	f3.close()
	f4.close()
	f5.close()
	f6.close()
	f7.close()
	f8.close()
	f9.close()

def escribir(word,f1,f2,f3,f4,f5,f6,f7,f8,f9,f0):
	if(word[len(word)-1]=='1'):
		f1.write(word+"\n")
	elif(word[len(word)-1]=='2'):
		f2.write(word+"\n")
	elif(word[len(word)-1]=='3'):
		f3.write(word+"\n")
	elif(word[len(word)-1]=='4'):
		f4.write(word+"\n")
	elif(word[len(word)-1]=='5'):
		f5.write(word+"\n")
	elif(word[len(word)-1]=='6'):
		f6.write(word+"\n")
	elif(word[len(word)-1]=='7'):
		f7.write(word+"\n")
	elif(word[len(word)-1]=='8'):
		f8.write(word+"\n")
	elif(word[len(word)-1]=='9'):
		f9.write(word+"\n")
	elif(word[len(word)-1]=='0'):
		f0.write(word+"\n")
	else:
		print("error")


main()