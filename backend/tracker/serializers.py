"""This file contains all the serializers for the tracker app
"""
from rest_framework import serializers
from tracker.models import Currency, Category


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
