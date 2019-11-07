from django.shortcuts import HttpResponse

def index (request):
	return HttpResponse("Hello,wordl")

# Create your views here.
