from datetime import timedelta
from time import sleep
from django.core.management.base import BaseCommand, CommandError

from django.utils.timezone import now
from bed.models import BedData,HospitalData


class Command(BaseCommand):
    def handle(self, *args, **options):
       
        BedData.create_available_beds()
        HospitalData.objects.all().delete()
        HospitalData.create_hospital_data()