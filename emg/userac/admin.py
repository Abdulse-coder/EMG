from django.contrib import admin
from . models import CustomUser
from pharmacy . models import PharmacyOrder
from patients . models import History,FreeHistory,Chart,Medication,Order,Consent,Intervention
from managment . models import WardAdmissionDischarge


# Register your models here.
admin.site.register(CustomUser)
admin.site.register(History)
admin.site.register(FreeHistory)
admin.site.register(Chart)
admin.site.register(Medication)
admin.site.register(Order)
admin.site.register(Consent)
admin.site.register(Intervention)
admin.site.register(WardAdmissionDischarge)




