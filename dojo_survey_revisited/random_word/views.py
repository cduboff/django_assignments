from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

def word(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    request.session['word'] = get_random_string(length = 14),
    return render(request, 'word.html')

def reset(request):
    request.session.flush()
    return redirect('/word/random_word')
# Create your views here.
