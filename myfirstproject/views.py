import operator

from django.shortcuts import render
from pyexpat.errors import messages
from . import counter


def home(request):
	return render(request, 'index.html',{'key1':'I am coming from python code'})
def result(request):
	roll_num = request.GET.get('roll_number')
	score = request.GET.get('marks')
	message = f'Roll number: {roll_num} get {score} marks'
	return render(request, 'result.html', {'name': message})
def name(request):
	return render(request, 'name.html')
def about(request):
	article = request.GET['article']
	sorted_article, count = counter.count(article)
	return render(request, 'about.html', {'article':article, 'count':count,'article_dic':sorted_article})
def fruit(request):
	return render(request, 'fruit.html')
def prize(request):
	name = request.GET.get('buyer_name')
	range = request.GET.get('buyer_range')
	message = f'Dear {name}! Your range is {range}.'
	return render(request, 'prize.html', {'name':message})
