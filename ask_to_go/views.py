from django.shortcuts import render, render_to_response

# Create your views here.
def mainpage (request):
    name = 'duset daram'
    return render_to_response ('index.html',locals())

