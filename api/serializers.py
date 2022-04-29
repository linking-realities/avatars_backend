from rest_framework.serializers import ModelSerializer
from .models import *


class Ip2AsnSerializer(ModelSerializer):
    class Meta:
        model = Ip2Asn
        fields = ['as_number', 'range_start', 'as_description', 'country_code']


class Ip2CountrySerializer(ModelSerializer):
    class Meta:
        model = Ip2Country
        fields = ['range_start','range_end','country_code']

