from .models import *
from rest_framework import serializers


class BeerStyleSubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerStyleSubcategory
        fields = ('id', 'name')


class BeerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerDetail
        fields = ('id', 'description', 'must_specify')


class BeerStyleSerializer(serializers.ModelSerializer):
    subcategories = BeerStyleSubcategorySerializer(many=True)
    beer_details = BeerDetailSerializer(many=True) 

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'subcategories', 'beer_details')
