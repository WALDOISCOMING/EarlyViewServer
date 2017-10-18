'''
Created on 2017. 8. 27.
a
@author: kil kyung wan
'''
from django.contrib import admin
from .models import Company
from .models import CompanyImage


admin.site.register(Company)

admin.site.register(CompanyImage)

