from django.shortcuts import render
from rest_framework import viewsets
from api.models import Ip2Asn
from api.serializers import Ip2AsnSerializer
from django_filters.rest_framework import DjangoFilterBackend


class Ip2AsnViewSet(viewsets.ModelViewSet):
    # TODO: distinc query fields
    http_method_names = ['get']
    queryset = Ip2Asn.objects.all()
    serializer_class = Ip2AsnSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id', 'as_number']

# Create your views here.
