from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse


def index(request):
	html = render_to_string("index.html")
	return HttpResponse(html)

class Person(object):
	def __init__(self, username):
		self.username = username

def login(request):
	p = Person("ArthurY")
	context = {'username': 'Arthur'}
	cont = {'person': p}
	return render(request, 'login.html', context=cont)