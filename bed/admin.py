from django.contrib import admin
from .models import BedData, HospitalData
# Register your models here.

class AccessInline(admin.TabularInline):
    model = HospitalData


class VechileAdmin(admin.ModelAdmin):
    list_display = ['name','hospital_type','updated_at','total','vacant','occupied','bed_type',"oxygen_left_days","oxygen_left_hour"]

    search_fields = ['name', 'hospital_type',]
    readonly_fields = ['created_at', 'updated_at']
    list_filter = ['bed_type']
    inlines = [AccessInline]
    

admin.site.register(BedData, VechileAdmin)



class HospitalAdmin(admin.ModelAdmin):
    list_display = ['name','hospital_type','updated_at']
    search_fields = ['name', 'hospital_type',]
    readonly_fields = ['created_at', 'updated_at']
   
    

admin.site.register(HospitalData, HospitalAdmin)
