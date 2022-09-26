from django.http import HttpResponse
from django.shortcuts import render


def calculate():
    x = 1
    y = 2
    return x


# Create your views here.
def say_hello(request):
    # return HttpResponse('Hello World')
    x = calculate()
    y = 2
    return render(request, 'hello.html', {'name': 'kiefer'})
