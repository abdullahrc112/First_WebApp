import operator

from django.shortcuts import render
from pyexpat.errors import messages
from . import counter, ginti, vwls, palindrome_checker, calculate



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
def naam(request):
	return render(request, 'naam.html')
def urf(request):
	para = request.GET['para']
	num_lfz, sorted_para = ginti.gi(para)
	return render(request, 'urf.html',{'para':para,'num_lfz':num_lfz, 'sorted_para':sorted_para})
def text(request):
	return render(request, 'text.html')
def count(request):
	text = request.GET.get('text','')
	total_vowels, sorted_vowels = vwls.vwl(text)
	return render(request, 'count.html', {'text':text, 'total_vowels':total_vowels, 'sorted_vowels':sorted_vowels})
def word(request):
	return render(request, 'word.html')
def pali_checker(request):
	word = request.GET.get('word')
	palindrome = palindrome_checker.pali_check(word)
	return render(request, 'pali_checker.html', {'word':word, 'palindrome':palindrome})
def calculator(request):
	return render(request, 'calculator.html')
def calculator_result(request):
	num1 = request.GET.get('num1')
	num2 = request.GET.get('num2')
	operation = request.GET.get('operation')
	result = calculate.calculator_result(num1, num2, operation)
	return render(request, 'calculator_result.html', {'num1':num1,'num2':num2,'operation':operation,'result':result})













