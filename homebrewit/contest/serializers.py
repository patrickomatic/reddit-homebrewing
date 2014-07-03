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


class EntryBeerDetailSerializer(ModelSerializer):
    beer_detail = BeerDetailSerializer

    class Meta:
        model = EntryBeerDetail
        fields = ('id', 'beer_detail', 'value')


class EntrySerializer(ModelSerializer):
    style = BeerStyleSerializer
    #entry_beer_details = EntryBeerDetailSerializer(many=True)

    class Meta:
        model = Entry
        fields = ('style', 'beer_name', 'special_ingredients') # XXX , entry_beer_details
        read_only_fields = ('id', 'user', 'winner', 'rank', 'score', 'received_entry')
