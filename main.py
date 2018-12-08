from flask import Flask,render_template,request
import pyttsx3
from nltk import word_tokenize,sent_tokenize
import pythoncom
import multiprocessing
import subprocess
import time
from scripts import sentiment
#from forms import RegistrationForm
pythoncom.CoInitialize()
f = open("intro.txt")
egsen=f.read()
words=sent_tokenize(egsen)
#print(words)
engine = pyttsx3.init()

app = Flask(__name__)
c,tques=0,5
def firs():
	for i in words:
		engine.say(i)
	engine.runAndWait()
#p1=multiprocessing.Process(name="p1",target=firs)
@app.route("/")
def home():
	return render_template("start.html")

@app.route("/home",methods=['GET'])
def first():
	global p1
	p1=multiprocessing.Process(name="p1",target=firs)
	#p1.terminate()
	p1.start()
	return render_template("intro.html",your_list=words)
#def stop():

@app.route("/home",methods=["POST"])
def sec():
	#p1=multiprocessing.Process(name="p1",target=firs)
	p1.terminate()
	return render_template("intro.html",your_list=words)

@app.route("/interview",methods=["GET"])
def thir():
	return render_template("interview.html")


@app.route("/interview",methods=["POST"])
def four():
	global c
	global tques
	if c<tques:
		a=request.form['ans']
		sentiment.record(a)
		c+=1
		return render_template("interview.html")
	else:
		li=sentiment.yourresponses("first.txt")
		c=0
		return render_template("yourresponses.html",your_list=li)

@app.route("/endinterview",methods=["POST"])
def five():
	global tques
	li=sentiment.analyse("first.txt",tques)
	if li[5]==0:
		res="Negative"
	elif li[5]==1:
		res="Positive"
	elif li[5]==2:
		res="Neutral"
	return render_template("start.html")

"""@app.route("/Register")
def register():
	form = RegistrationForm()
	return render_template("Register.html",title='Register',form=form)
"""
