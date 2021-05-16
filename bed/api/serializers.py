
from rest_framework import serializers
from ..models import BedData,HospitalData
from django.contrib.auth.models import User
from rest_framework.response import Response





class HospitalDataSerializer(serializers.ModelSerializer):
   contact_number = serializers.SerializerMethodField()
   class Meta:
      model = HospitalData
      exclude=[]

   def get_contact_number(self, obj):
      return eval(obj.contact_number)



class BedDataSerializer(serializers.ModelSerializer):
   # pdf_data = HospitalDataSerializer(source="hospitaldata_set", many=True, read_only=True)
   total = serializers.SerializerMethodField()
   vacant = serializers.SerializerMethodField()
   occupied = serializers.SerializerMethodField()
   oxygen_left_days = serializers.SerializerMethodField()
   oxygen_left_hour = serializers.SerializerMethodField()
   class Meta:
      model = BedData
      exclude=[]

   def get_total(self, obj):
      return eval(obj.total)

   def get_vacant(self, obj):
      return eval(obj.vacant)

   def get_occupied(self, obj):
      return eval(obj.occupied)
   
   def get_oxygen_left_hour(self, obj):
      return eval(obj.oxygen_left_hour) if obj.oxygen_left_hour else None

   def get_oxygen_left_days(self, obj):
      return eval(obj.oxygen_left_days) if obj.oxygen_left_days else None

