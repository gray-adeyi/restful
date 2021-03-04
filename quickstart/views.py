from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions
from . import serializers
from django.contrib.auth import models as dj_model

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or editted
    """
    queryset = dj_model.User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]
     

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or editted
    """
    queryset = dj_model.Group.objects.all()
    serializer_class = serializers.GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
