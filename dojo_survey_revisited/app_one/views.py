from django.shortcuts import render, HttpResponse, redirect

def index(request):
    return render(request, 'index.html')
def result(request):
    request.session['name'] = request.POST['name']
    request.session['loc'] = request.POST['location']
    request.session['lang'] = request.POST['favorite_language']
    request.session['comment'] = request.POST['comment']
    return redirect('/result')
# def result(request):
#     if request.method == "GET":
#         print(request.GET)
#     if request.method == "POST":
#         context = {
#             'name': request.POST['name'],
#             'lang': request.POST['favorite_language'],
#             'loc': request.POST['location'],
#             'comment': request.POST['comment'],
#         }
#         return render(request, 'result.html', context)
#     return redirect('/result')
# Create your views here.
