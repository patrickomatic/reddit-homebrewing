from .models import *
from rest_framework import serializers


class BeerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerDetail
        fields = ('id', 'type', 'description', 'must_specify')


class BeerStyleSubcategorySerializer(serializers.ModelSerializer):
    beer_details = BeerDetailSerializer(many=True) 

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'subcategories', 'beer_details')


class BeerStyleSerializer(serializers.ModelSerializer):
    subcategories = BeerStyleSubcategorySerializer(many=True)
    beer_details = BeerDetailSerializer(many=True) 

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'subcategories', 'beer_details')
