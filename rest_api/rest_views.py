from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import (filters, generics, permissions, renderers,
                            response, schemas, viewsets)
from rest_framework.decorators import api_view, action, renderer_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework_swagger.renderers import OpenAPIRenderer, SwaggerUIRenderer
 
from rest_api.permissions import IsOwnerOrReadOnly
from rest_api.serializers import *
from .models import *
 

@api_view()
@renderer_classes([SwaggerUIRenderer, OpenAPIRenderer])
def schema_view(request):
    generator = schemas.SchemaGenerator(title='Rest API')
    return response.Response(generator.get_schema(request=request))

def index(request):
    return HttpResponse("Rest API")


#[Start] Override one of the pagination classes, and seting the attributes..
class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 1000

#[end]




class WalletViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = WalletTable.objects.all()
    serializer_class = WalletTableSerializer

    #Apply Filter..
    filter_backends = (DjangoFilterBackend, OrderingFilter, SearchFilter)
    
    filterset_fields = ['wallet_id']
    #Apply Sorting..
    ordering_fields = ['create_at']
    #Serchalble Fields..
    search_fields = ['user_id']
 