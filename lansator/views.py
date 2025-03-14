from django.shortcuts import render
from datetime import datetime
from django.http import HttpResponse
import locale
# Create your views here.


def zile_pana_la_lansare(request):
    return HttpResponse('Mai sunt 10 zile pana la lansare')

def nume_racheta_view(request):
    return HttpResponse("Numele rachetei este Corina")

def racheta_template_view(request):
    return render(request, "index.html")

luni = ["Ianuarie", "Februarie", "Martie", "Aprilie", "Mai", "Iunie", "Iulie", "August", "Septembrie", "Octombire", "Noiembrie", "Decembrie"]

locale.setlocale(locale.LC_TIME, "ro_RO")

def today_view(request):
    today = datetime.today()
    year = today.year
    month = today.month
    day = today.day

    context = {
        'data' : f'{day}-{luni[month-1]}-{year}'
    }
    return render(request, "data.html", context)