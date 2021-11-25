from django.shortcuts import render
from .tasks import test_func
from django.http import HttpResponse

# Create your views here.
def test(request):
	test_func.delay()
	return HttpResponse("Done")

def test_views(request):
	return render(request, "mainapp.html", {})

def other_view(request):
	print(request)
	print(request.FILES)
	return render(request, "other.html", {})