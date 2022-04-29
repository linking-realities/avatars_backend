from django.shortcuts import render
from rest_framework import viewsets
from api.models import Ip2Asn, Ip2Country
from api.serializers import Ip2AsnSerializer, Ip2CountrySerializer
from django_filters.rest_framework import DjangoFilterBackend


class Ip2AsnViewSet(viewsets.ModelViewSet):

    http_method_names = ['get']
    queryset = Ip2Asn.objects.values('range_start', 'as_number','as_description','country_code').distinct()
    serializer_class = Ip2AsnSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'as_number','range_start']


class Ip2CountryViewSet(viewsets.ModelViewSet):

    http_method_names = ['get']
    queryset = Ip2Country.objects.values('range_start','range_end','country_code').distinct()
    serializer_class = Ip2CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'range_start']

