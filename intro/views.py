from django.shortcuts import render
import pyttsx3
import pythoncom
import multiprocessing
# Create your views here.

def intro(request):
	global fread,p1
	
	fo = open("intro.txt")
	fread = fo.read()
	fo.close()
	
	
	args = {"content":fread}
	return render(request,'intro/home.html',args)
