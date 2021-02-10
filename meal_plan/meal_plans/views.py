from django.shortcuts import render

# Create your views here.

def index(request):
    '''Домашняя страница приложения'''
    return render(request, 'meal_plans/index.html')