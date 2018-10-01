from flask import Flask,render_template
import pyttsx3
from nltk import word_tokenize,sent_tokenize
import pythoncom
import multiprocessing
import subprocess
import time
from forms import RegistrationForm
pythoncom.CoInitialize()
f = open("intro.txt")
egsen=f.read()
words=sent_tokenize(egsen)
#print(words)
engine = pyttsx3.init()

app = Flask(__name__)

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

@app.route("/Register")
	def register():
		form = RegistrationForm()
		return render_template("Register.html",title='Register',form=form)

