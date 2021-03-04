# serializers.py

""" Helps to serialize django model
    instances abd queryset to json
    and vice versa via deserialization
"""

from django.contrib.auth.models import User, Group
from rest_franework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','username','email','groups']


class GroupSerializer(serializer.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
