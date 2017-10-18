'''
Created on 2017. 8. 27.
a
@author: kil kyung wan

'''

from django.db import models



class Category(models.Model):
    '''
    CATEGORY_NAME_TYPE=(
        ("전기","전기"),
        ("가전","가전"),

    )
    '''     
    category_name=models.CharField(max_length=30) 
    def __str__(self):
        return self.category_name