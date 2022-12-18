from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')


from django.http import JsonResponse

def check(request):
    num = int(request.GET.get('num', None))
    responce = {}
    if num % 2 ==0:
        responce = {"even":True}
    else:
        responce = {"even":False}

    return JsonResponse(responce)