from django.shortcuts import render

# python manage.py runserver 0.0.0.0:8000
 
def hello(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'hello.html', context)