from rest_framework.decorators import api_view
# from rest_framework.response import  
from django.http import HttpResponse

@api_view(['GET'])
def health_check(request) :
    return HttpResponse(
        '{"status" : " django Backend is running"}')
    
