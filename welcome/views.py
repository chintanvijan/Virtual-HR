from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm
from .models import userinfo
import time
# Create your views here.

def home(request):
	if request.method == 'POST':
		form = UserRegistrationForm(request.POST,request.FILES)
		if form.is_valid():
			username = form.cleaned_data.get('email')
			filename = form.cleaned_data.get('fileinput')
			form.save()
			idi = form.cleaned_data.get('id')
			formobj = userinfo(idi,username,filename)
			formobj.save()
			messages.success(request,f'Your account has been created.Login to continue!')
			return redirect('signin')
	else:
		form = UserRegistrationForm()
	args = {'form':form}
	return render(request,'home.html',args)