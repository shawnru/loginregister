
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
# from django import http

def index(request):
    try:
        request.session['counter'] += 0
    except TypeError:
        request.session['counter'] = 0
    return render(request, 'first_app/index.html')

def postresult(request):
    if request.method == 'POST':
        if request.POST['submit']:
            request.session['counter'] += 1
            request.session['name'] = request.POST['name']
            request.session['dloc'] = request.POST['dloc']
            request.session['favlang'] = request.POST['favlang']
            request.session['comments'] = request.POST['comments']
    return redirect('/result')

def result(request):
    return render(request, 'first_app/result.html')

# def session_test_1(request):
#     request.session['test'] = 'Session Vars Worked!'
#     return http.HttpResponseRedirect('done/?session=%s' % request.session.session_key)
#
# def session_test_2(request):
#     return http.HttpResponse('<br>'.join([
#         request.session.session_key,
#         request.GET.get('session'),
#         request.session.get('test', 'Session is Borked :(')
#          ]))
