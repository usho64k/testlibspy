def mathMod(value=10,valueMax=10):	#Type:string
	retstr = ""
	while value*10<valueMax:
		retstr+="0"
		value*=10
	return retstr;

def mkstr(repeat=1):	#Type:string
	retstr = "";	#Type:string
	i = 1;		#Type:int
	while i<=repeat:
		retstr+=mathMod(i,repeat)
		retstr+=str(i)
		retstr+="\r\n"
		i+=1
	return retstr;

f = open('file.txt','w')
mem = mkstr(1000)
f.write(mem)
f.close()
print "success"
