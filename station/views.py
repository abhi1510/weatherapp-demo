from django.shortcuts import render
from .models import Reading 

def home(request):
	data = Reading.objects.last()
	return render(request, 'index.html', {'data':data}) 
