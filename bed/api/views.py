from .serializers import BedDataSerializer,HospitalDataSerializer
from ..models import BedData,HospitalData
from rest_framework.views import APIView
from rest_framework import permissions, generics

from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import django_filters.filters
import django_filters.rest_framework
from rest_framework import filters


class ViewBedss(generics.ListAPIView):
    serializer_class = BedDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'name': ['icontains'],
        'hospital_type': ['icontains']
    }

    def get_queryset(self):
        queryset = BedData.objects.all()
        return queryset

class ViewHospitals(generics.ListAPIView):
    serializer_class = HospitalDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'name': ['icontains'],
        'hospital_type': ['icontains']
    }

    def get_queryset(self):
        queryset = HospitalData.objects.all()
        return queryset