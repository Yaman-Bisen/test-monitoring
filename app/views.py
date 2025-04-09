from django.shortcuts import render
from django.http import JsonResponse
from .models import *
# Create your views here.


def index(request):
    return JsonResponse({
        'status': True,
        'message': 'Hello world!!!'
    })

def create_user(request, number):
    metrics = number % 10
    message = 'DB operation failed.'
    status_code = 400
    status = False

    if not metrics:
        UserModel.objects.create(
            username='test',
            age=25
        )
        message= 'User created successfully.'
        status_code = 200
        status = True
    
    return JsonResponse({
        'status': status,
        'message': message
    }, status_code=status_code)