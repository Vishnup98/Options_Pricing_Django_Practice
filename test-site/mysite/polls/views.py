from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import loader
from .models import BS_option

# def index(request):
#     options_list = BS_option.objects.order_by("time_to_maturity")
#     output=""
#     for i in options_list:
#         output += "Black Scholes Analytic Option Price for option with parameters\n"
#         output += i.__repr__()+"\n"
#         output += "is: " + str(i.analytic_price()) +"\n\n\n\n\n"
#     return HttpResponse(output, content_type="text/plain")

#     return HttpResponse(output)

def index(request):
    options_list=BS_option.objects.order_by("time_to_maturity")
    template=loader.get_template("polls/index.html")
    context={"options_list" : options_list}
    return HttpResponse(template.render(context,request))

def price(request,option_id):
    try:
        option=BS_option.objects.get(id=option_id)
    except BS_option.DoesNotExist:
        raise Http404("Option does not exist!")

    output=""
    output += "Black Scholes Analytic Option Price for option with parameters\n"
    output += option.__repr__()+"\n"
    output += "is: " + str(option.analytic_price()) +"\n\n\n\n\n"

    return HttpResponse(output,content_type="text/plain")