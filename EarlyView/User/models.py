'''
Created on 2017. 11. 03.

@author: kil kyung wan
유저의 DB 만들기.

'''

from Category.models import Category
from django.db import models

class NormalUser(models.Model):
    
    
    
    #난 이것이 더 맞다 생각됨.
   # category=[]
    """
    유저 table
    .number
    .email
    .category
    .birthday
    .password
    """   
    username =models.CharField(max_length=30,default='a')
    email =models.EmailField(blank=False,default='a@a.com')
    category = models.CharField(max_length=30,default='a')
    birthday = models.DateField(blank=False)
    

       


