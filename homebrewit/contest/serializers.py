from .models import *
from rest_framework import serializers


class BeerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BeerDetail
        fields = ('id', 'type', 'description', 'must_specify')


class BeerStyleSerializer(serializers.ModelSerializer):
    beer_details = BeerDetailSerializer(many=True) 
    can_enter = serializers.BooleanField(source='can_enter', read_only=True)
    has_subcategories = serializers.BooleanField(source='has_subcategories', read_only=True)

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'can_enter', 'has_subcategories', 'beer_details')
