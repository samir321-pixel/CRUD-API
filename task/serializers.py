from rest_framework import serializers
from .models import *


class user_data_serializer(serializers.ModelSerializer):
    class Meta:
        model = user_data
        fields = '__all__'
