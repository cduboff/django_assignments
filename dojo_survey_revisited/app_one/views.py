from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')
def show(request):
    if request.method == 'GET':
        return redirect('/')
    request.session['result'] = {
        'name': request.POST['name'],
        'loc': request.POST['location'],
        'lang': request.POST['favorite_language'],
        'comment': request.POST['comment'],
    }
    return redirect('/result')
def result(request):
    context = {
        'result': request.session['result']
    }
    return render(request, 'result.html', context)
# Create your views here.
