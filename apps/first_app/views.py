
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages

def index(request):
    context = {
        'all_users': User.objects.all()
    }
    print User.objects.all()
    return render(request, 'first_app/index.html', context)

def register(request):
    if request.method == 'POST':
        if request.POST['register']:
            response_from_models = User.objects.register(request.POST)
            try:
                if response_from_models['errors']:
                    for error in response_from_models['errors']:
                        messages.error(request, error)
                        return redirect('/')
                else:
                    return redirect('/success')
            except KeyError:
                return redirect('/success')

def success(request):

    return render(request, 'first_app/success.html')


def login(request):
    if request.method == 'POST':
        # try:
        User.objects.signin(request.POST)
        if User.objects.signin(request.POST):
            return redirect('/success')
        else:
            messages.error(request, 'No user in database')
            return redirect ('/')
        # except AttributeError:
            # messages.error(request, 'No user in database')
            # return redirect ('/')

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
