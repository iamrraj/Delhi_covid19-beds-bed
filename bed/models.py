from django.db import models
from django.utils.translation import ugettext_lazy as _, ugettext
# Create your models here.
from django.contrib.auth.models import User
import uuid
import json 
import requests
import os
from dotenv import load_dotenv

load_dotenv()

class BedData(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    name =  models.CharField(_("Hospital Name"), max_length=240, blank=True, null=True)
    hospital_type = models.CharField(_("Hospital Type"), max_length=240, blank=True, null=True)
    update = models.CharField(_("Update date time"), max_length=240, blank=True, null=True)
    total = models.CharField(_("Total Beds"), max_length=240, blank=True, null=True)
    bed_type = models.CharField(_("Bed Types"), max_length=240, blank=True, null=True)
    occupied = models.CharField(_("Total Occupied beds"), max_length=240, blank=True, null=True)
    vacant = models.CharField(_("Total Vacant beds"), max_length=240, blank=True, null=True)
    oxygen_left_days = models.CharField(_("Total Days oxygen Left"), max_length=240, blank=True)
    oxygen_left_hour = models.CharField(_("Total Hours oxygen Left"), max_length=240, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Hospital Bed data'

    # @classmethod
    def create_available_beds():
        url = os.getenv("BEDS")
        request_data = requests.get(url)
        data=request_data.text
        obj = data[data.find('{') : data.rfind('}')+1]
        jsonObj = json.loads(obj)

        data = ["beds", "covid_icu_beds","ventilators","oxygen_beds","icu_beds_without_ventilator","noncovid_icu_beds"]
        for d in data:
            for k, v in jsonObj[d].items():
                if "type" in v:
                    BedData.objects.update_or_create(
                        bed_type=d,
                        name=k,
                        defaults={
                            "hospital_type": v["type"],
                            "update": v["last_updated_at"],
                            "total": v["total"],
                            "occupied": v["occupied"],
                            "vacant": v["vacant"],

                        }
                    )

        # Get Oxygen Data now:
        for k, v in jsonObj["oxygen_left_for"].items():
            bed_data = BedData.objects.filter(name__icontains=k)
            for bed in bed_data:
                if bed:
                    bed.oxygen_left_days = v["days"]
                    bed.oxygen_left_hour = v["hours"]
                    bed.save()

            
               

    

    
class HospitalData(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    bed = models.ForeignKey(BedData, models.CASCADE, verbose_name=_('bed'), null=True, blank=True)
    name =  models.CharField(_("Hospital Name"), max_length=240, blank=True, null=True)
    hospital_type = models.CharField(_("Hospital Type"), max_length=240, blank=True, null=True)
    address = models.CharField(_("Hospital Address"), max_length=240, blank=True, null=True)
    contact_number = models.CharField(_("Hospital contact number"), max_length=240, blank=True, null=True)
    map_link = models.URLField(_("Hospital contact number"), max_length=840, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Hospital Data'

    

    def create_hospital_data():
        url = os.getenv("HOSPITAL")
        request_data = requests.get(url)
        data=request_data.text
        obj = data[data.find('{') : data.rfind('}')+1]
        jsonObj = json.loads(obj)
        for k, v in jsonObj.items():
            bed_data = BedData.objects.filter(name__icontains=k).first()
            
            if bed_data:
                HospitalData.objects.update_or_create(
                    name=k,
                    defaults={
                        "bed":bed_data,
                        "hospital_type": v["type"],
                        "address": v["address"],
                        "contact_number": v["contact_numbers"],
                        "map_link": v["location"],
                    }
                )

  
       
        