from .models import *
from rest_framework.serializers import ModelSerializer, BooleanField


class BeerDetailChoiceSerializer(ModelSerializer):
    class Meta:
        model = BeerDetailChoice
        fields = ('id', 'name')


class BeerDetailSerializer(ModelSerializer):
    choices = BeerDetailChoiceSerializer(many=True)

    class Meta:
        model = BeerDetail
        fields = ('id', 'type', 'description', 'must_specify', 'choices')


class BeerStyleSerializer(ModelSerializer):
    beer_details = BeerDetailSerializer(many=True) 
    can_enter = BooleanField(source='can_enter', read_only=True)
    has_subcategories = BooleanField(source='has_subcategories', read_only=True)

    class Meta:
        model = BeerStyle
        fields = ('id', 'name', 'can_enter', 'has_subcategories', 'beer_details')
