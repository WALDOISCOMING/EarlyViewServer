# -*- coding: utf-8 -*-
'''
Created on 2017. 8. 27.

@author: kil kyung wan
Company의 DB 만들기.

'''
from django.db import models
from Category.models import Category


#사진 저장을 위해서 os  impoty
import os

# Create your models here.

"""
def get_image_path(instance,filename):
    return os.path.join('EarlyView','Company','photo',filename)
a
"""

class Company(models.Model):
    #난 이것이 더 맞다 생각됨.
   # category=[]
    """
    회사 table
    .카테고리 (외래키)
    .회사 이름  
    .회사 내용
    ----회사 사진 table
        .회사(외래키)
        .회사 사진 사진
    """   
  
    company_category =  models.ManyToManyField(Category)
    # 외래키로 할려면. category =  models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)    
    company_name = models.CharField(max_length=30)
    company_content = models.CharField(max_length=30)
  
       
    def __str__(self):
        return '회사명:<'+self.company_name+'>'

class CompanyImage(models.Model):
    companyImage_company = models.ForeignKey(Company,null=True)
    companyImage_image = models.ImageField()
    
    def __str__(self):
        return self.companyImage_company.company_name+"의 사진"

