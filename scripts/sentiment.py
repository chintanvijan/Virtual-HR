from textblob import TextBlob

def analyse(f,tques):
	fname = "answers\\"+f
	negc,posc,neu=0,0,0
	fi = open(fname)
	sen = fi.read().split("\n__\n")
	for i in sen:
		seni = i.split(".")
		res = TextBlob(seni)
		#print(res.sentiment())
		#print(res)
		if res.sentiment.polarity <0:
			negc+=1
		elif res.sentiment.polarity>0:
			posc+=1
		elif res.sentiment.polarity==0:
			neu+=1
	li=[negc,posc,neu]
	fi.close()
	nper = (li[0]*100)/tques
	pper = (li[1]*100)/tques
	li.append(nper)
	li.append(pper)
	if nper>pper:
		li.append(0)
	elif pper>nper:
		li.append(1)
	elif nper==pper:
		li.append(2)
	return li

def record(t):
	fi = open("answers\\First.txt","a")
	fi.write(t)
	fi.write("\n__\n")
	fi.close()

def yourresponses(f):
	fname="answers\\"+f
	fi=open(fname)
	tr=fi.read().split("\n__\n")
	return tr
