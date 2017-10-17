from django.contrib import admin
from .models import LiquorList   
# Register your models here.

admin.site.register(LiquorList)  ## Registering the imported model to the admin area
