from django.shortcuts import render
from django.http import request
from django.http import HttpResponse
# Create your views here.

def index(request):
    value = "This is a Project to Count the Number of Words"
    return render(request, 'index.html', {'value': value})


def counter(request):
    text = request.POST['text']
    amount_of_words = len(text.split())
    return render(request, 'counter.html', {'amount': amount_of_words})