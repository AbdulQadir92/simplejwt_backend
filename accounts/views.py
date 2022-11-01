from django.shortcuts import render
from django.contrib.auth.models import User, auth

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def register_user(request):
    data = request.data
    username = data['username']
    email = data['email']
    password1 = data['password1']
    password2 = data['password2']

    if password1 == password2:
        if User.objects.filter(username=username).exists():
            return Response({'message': 'Username is already taken'})
        elif User.objects.filter(email=email).exists():
            return Response({'message': 'Email is already taken'})
        else:
            User.objects.create_user(
                username=username, password=password1, email=email)
            user = auth.authenticate(username=username, password=password1)
            if user is not None:
                auth.login(request, user)
            else:
                return Response({'message': 'Something went wrong'})

            return Response({'message': 'User created successfully'})
    else:
        return Response({'message': 'Passwords do not match'})
