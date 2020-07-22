from django.shortcuts import render, HttpResponse, redirect
def index(request):
    return render(request, 'index.html')
def result(request):
    if request.method == "GET":
        print(request.GET)
    if request.method == "POST":
        context = {
            'name': request.POST['name'],
            'lang': request.POST['languages_known'],
            'loc': request.POST['location'],
            'comment': request.POST['comment'],
        }
        return render(request, 'result.html', context)
    return render(request, 'result.html')
# Create your views here.
