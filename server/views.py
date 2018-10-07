# users/views.py
from rest_framework import generics

from . import models
from . import serializers
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render
from rest_framework.decorators import api_view

class UserListView(generics.ListCreateAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
