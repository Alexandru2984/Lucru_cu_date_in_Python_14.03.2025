from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def zile_pana_la_lansare(request):
    return HttpResponse('Mai sunt 10 zile')