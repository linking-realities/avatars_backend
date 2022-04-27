from rest_framework.serializers import ModelSerializer
from .models import *


class Ip2AsnSerializer(ModelSerializer):
    class Meta:
        model = Ip2Asn
        fields = ['as_number', 'as_description', 'country_code']
