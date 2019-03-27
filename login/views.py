from django.shortcuts import render,redirect
from . import forms
import sqlite3
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .scripts import faceverify
import time
from .models import userimg
import cv2
from textblob import TextBlob
import pythoncom
import pyttsx3
from django.contrib import messages
# Create your views here.
#row=[]
c=0
def face(request):
	global c
	pythoncom.CoInitialize()
	engine=pyttsx3.init()
	emai=request.user.email
	conn = sqlite3.connect("db.sqlite3")
	cur = conn.cursor()
	cur.execute("select fileinput from welcome_userinfo where email=? ",(emai,))
	row = cur.fetchall()
	print(row[0][0])
	conn.close() 
	facecom = faceverify.comp(row[0][0])
	print(facecom)
	if facecom == True:
		fname = 'answers\\'+emai+".txt"
		fi = open(fname,'w')
		fi.close()
		fi =open('questions.txt')
		fread = fi.read()
		fi.close()
		questions = fread.split('\n__\n')
		engine.say(questions[0])
		print(c)	
		args = {'question':questions[0]}
		return render(request,'login/face.html',args)
	else:
		messages.success(request,f'Faces does not match!')
		return redirect('login')
def signin(request):
	
	return render(request,'login/home.html')

def tt(request):

	 i = request.FILES.get('image')  # get the image
	 idi = request.GET.get('id')
	 print(i)
	 PATH_TO_TEST_IMAGES_DIR = 'media/'
	 f = ('uk1.jpeg')
	 formobj = userimg(idi,i)
	 formobj.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
	 #i.save('%s/%s' % (PATH_TO_TEST_IMAGES_DIR, f))
	 return render(request,'login/facecapture.html')

def ghi(request):
	#form = forms.Person()
	global c
	pythoncom.CoInitialize()
	engine=pyttsx3.init()
	fi = open('questions.txt')
	fread = fi.read()
	fi.close()
	questions = fread.split('\n__\n')
	if request.method=="POST":
		#form = forms.Person()
		#picture = request.POST.get('picture')
		mean = request.POST.get('n1')
		print(mean)
		answer = request.POST.get('answers')
		print(answer) 
		c+=1
	if c>=len(questions):
		c=0
		negc,posc,neu = 0,0,0
		emai=request.user.email
		fname="answers\\"+emai+".txt"
		fi = open(fname)
		fread = fi.read()
		fi.close()
		answers = fread.split('\n__\n')
		for i in answers:
			seni = i.split(".")
			res = TextBlob(i)
			#print(res.sentiment())
			#print(res)
			if res.sentiment.polarity <0:
				negc+=1
			elif res.sentiment.polarity>0:
				posc+=1
			elif res.sentiment.polarity==0:
				neu+=1
		li=[negc,posc,neu]
		nper = (li[0]*100)/len(questions)
		pper = (li[1]*100)/len(questions)
		li.append(nper)
		li.append(pper)
		if nper>pper:
			li.append(0)
		elif pper>nper:
			li.append(1)
		elif nper==pper:
			li.append(2)
		print(li)
		return render(request,'login/logout.html')
	else:

		args = {'question':questions[c]}
		emai = request.user.email
		fname = "answers\\"+emai+".txt"
		fi = open(fname,'a')
		fi.write(answer)
		fi.write('\n__\n')
		fi.close()
		engine.say(questions[c])
		return render(request,'login/face.html',args)











