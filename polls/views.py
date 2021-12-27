from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
	return HttpResponse("<marquee><h1>Welcome to my website</h1></marquee>")