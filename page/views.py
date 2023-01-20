from django.shortcuts import render
from .forms import Question
# Create your views here.
import pandas as pd
import pickle
import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def if_yes_or_no(l):
	li = []
	for i in l:
		if i=='Yes':
			li.append(1)
		elif i=='No':
			li.append(0)
	return li

def testcovid(l):
	direct = os.getcwd() 
	di = direct + "/page/pred.pkl"
	d = open(di,'rb')
	data = pickle.load(d)
	return data.predict(l)

def covidfree(request):
	return render(request,'isfine.html',{})

def covidpositive(request):
	return render(request,'ispos.html',{})


def home(request):
	if request.method == 'POST':
		form = Question(request.POST)
		#print(BASE_DIR)
		if form.is_valid():
			gen = ["Yes","No"]
			dia = form.cleaned_data.get("Do_you_have_Diarrhea")
			fever = form.cleaned_data.get("Do_you_have_Fever")
			cough = form.cleaned_data.get("Are_you_experiencing_Coughing")
			bre = form.cleaned_data.get("Do_you_have_ShortnessOfBreath")
			sore = form.cleaned_data.get("Do_you_have_SoreThroat")
			nau = form.cleaned_data.get("Are_you_experiencing_NauseaVomitting")
			fat = form.cleaned_data.get("Do_you_have_Fatigue")
			
			message = "Hi Doctor, has requested "+gen[int(dia)-1]+gen[int(fever)-1]+gen[int(cough)-1]+gen[int(bre)-1]+gen[int(sore)-1]+gen[int(nau)-1]+gen[int(fat)-1]
			#return redirect('appointment')
			#print(message)
			list_response = [if_yes_or_no([gen[int(dia)-1],gen[int(fever)-1],gen[int(cough)-1],gen[int(bre)-1],gen[int(sore)-1],gen[int(nau)-1],gen[int(fat)-1]])]
			#print(list_response)
			res = testcovid(list_response)
			#print(res)
			if res[0] == 0:
				return render(request,'isfine.html',{})
			else:
				return render(request,'ispos.html',{})	
	else:
		form = Question()
	return render(request,'index.html',{"form":form})

		

def is_covid(request):
	if request.method == 'POST':
		form = Question(request.POST)
		if form.is_valid():
			gen = ["Yes","No"]
			dia = form.cleaned_data.get("Do_you_have_Diarrhea")
			fever = form.cleaned_data.get("Do_you_have_Fever")
			cough = form.cleaned_data.get("Are_you_experiencing_Coughing")
			bre = form.cleaned_data.get("Do_you_have_ShortnessOfBreath")
			sore = form.cleaned_data.get("Do_you_have_SoreThroat")
			nau = form.cleaned_data.get("Are_you_experiencing_NauseaVomitting")
			fat = form.cleaned_data.get("Do_you_have_Fatigue")
			
			message = "Hi Doctor, has requested "+gen[int(dia)-1]+gen[int(fever)-1]+gen[int(cough)-1]+gen[int(bre)-1]+gen[int(sore)-1]+gen[int(nau)-1]+gen[int(fat)-1]
			#return redirect('appointment')
			#print(message)
			list_response = [if_yes_or_no([gen[int(dia)-1],gen[int(fever)-1],gen[int(cough)-1],gen[int(bre)-1],gen[int(sore)-1],gen[int(nau)-1],gen[int(fat)-1]])]
			#print(list_response)
	else:
		form = Question()

	return render(request,"index.html",{"form":form})
