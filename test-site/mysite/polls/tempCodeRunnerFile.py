from django.shortcuts import render
from django.http import HttpResponse
from .models import BS_option

def index(request):
    options_list = BS_option.objects.order_by("time_to_maturity")
    output=""
    for i in options_list:
        output += "Black Scholes Analytic Option Price for option with parameters\n "
        output += i()+"\n"
        output += "is: " + str(i.analytic_price())
    return HttpResponse(output)

    return HttpResponse(output)

def detail(request,option_id):
    return HttpResponse("You're looking at option %s." % option_id)
