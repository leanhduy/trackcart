"""This file contains all the serializers for the tracker app
"""
from rest_framework import serializers
from tracker.models import Currency

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"
