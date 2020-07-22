from django.shortcuts import render
from time import localtime, strftime

def index(request):
    context = {
        "time": strftime("%c %p", localtime())
    }
    return render(request, 'index.html', context)

# Create your views here.
