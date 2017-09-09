# -*- coding: utf-8 -*-
'''
Created on 2017. 8. 30.

@author: kil kyung wan
'''
from Company.models import Company
from Company.models import CompanyImage
from rest_framework import viewsets, status

from Company.serializers import PhotoSeializer



#crsf post �� ���� �ʿ���
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from Company.serializers import CompanySerializer    

#detail�� ���Ͽ� �ʿ���.
from rest_framework.decorators import detail_route, permission_classes
#�۹̼�
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TaskViewSet(viewsets.ModelViewSet):
    
    queryset = CompanyImage.objects.order_by('-id')
    serializer_class = PhotoSeializer
    
    
class CompanyViewSet(viewsets.ModelViewSet):
    
     
    queryset = Company.objects.order_by('-id')
    serializer_class = CompanySerializer
    
    @detail_route(methods=['get'],permission_classes=[IsAuthenticatedOrReadOnly],url_path='companycategoryfilter')    
    def companyCategoryfilter(self,request,pk=None):

            
        api_result = Company.objects.filter(company_category=pk).order_by('-id')
        serializer_class = CompanySerializer(api_result,many=True)
        return Response(serializer_class.data)
        
        
    @detail_route(methods=['get'],permission_classes=[IsAuthenticatedOrReadOnly],url_path='companynamefilter')    
    def companyNamefilter(self,request,pk=None):
        
        api_result = Company.objects.filter(company_name=pk).order_by('-id')
        serializer_class = CompanySerializer(api_result,many=True)
        return Response(serializer_class.data)
        
    """
    @csrf_exempt
    def snippet_list(self,request):

        if request.method == 'GET':
            snippets = Company.objects.all()
            serializer = CompanySerializer(snippets, many=True)
            print (serializer.data)
            return JsonResponse(serializer.data, safe=False)

        elif request.method == 'POST':
            data = JSONParser().parse(request)
            serializer = CompanySerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)
            return JsonResponse(serializer.errors, status=400)
    """

    """
    def get(self, request, format=None):
        photo = CompanyImage.objects.all()
        serializer = PhotoSeializer(data=request.data)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
       serializer = PhotoSeializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def pre_save(self, obj):
        obj.owner = self.request.user
        

    def init(self, instance=None, data=empty, *kwargs):
        super(serializers.ModelSerializer, self).init(instance=instance, data=data, *kwargs)
    """
    """
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    def test(self,request,format=None):
        serializer_class = PhotoSeializer(data=request.DATA, files=request.FILES)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer_class.errors,status=status.HTTP_201_CREATED)

    """
 

