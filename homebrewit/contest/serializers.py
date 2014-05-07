from .models import *
from rest_framework import serializers


class BeerStyleSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerStyleSubcategory
        fields = ('id', 'name')

class BeerStyleSerializer(serializers.ModelSerializer):
    subcategories = BeerStyleSubcategorySerializer(many=True)

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'subcategories')
