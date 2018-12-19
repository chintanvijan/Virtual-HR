import speech_recognition as sr
import pocketsphinx
import sphinxbase
r=sr.Recognizer()
with sr.Microphone() as source:
	print("say")
	r.adjust_for_ambient_noise(source)
	audio=r.listen(source)
#print(audio)
	try:
		#res = audio.decode('utf-8')
		#t=r.recognize_houndify(audio,client_id="XwUuSYsqPcJLnY26C6Slsw==",client_key="cgAwf0Mgk4Qa2B_F6Xaii5gVhJgBIpOiLu1NaRODHwuNZ8dSnZhlmaiaom61ybsAKjMRM7DLwQsFEDr6Jp0rRQ==")
		t=r.recognize_google(audio)
		print("You said: " + t)
	except sr.UnknownValueError:
		print("Google Speech Recognition could not understand audio")
	except sr.RequestError as e:
		print("Could not request results from Google Speech Recognition service; {0}".format(e))
#print(sr.Microphone.list_microphone_names())
