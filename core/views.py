from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import supabase,os
from .utils import hash_base_62
from supabase import create_client, Client
from django.http import HttpResponseRedirect

# Create your views here.

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url,key)

@api_view(['POST'])
def create_url(request):
    short_code = hash_base_62.generate_random_base62_hash()
    try:
        response = (
        supabase.table("urls")
        .insert({"original_url": str(request.data["original_url"]), "short_code": short_code})
        .execute()
    )
        return Response({"message":"successfully stored","data":response.data},status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def redirect_to_url(request,short_code):
    code = short_code
    try:
        response = (
    supabase.table("urls")
    .select("*")
    .eq("short_code", code)
    .execute()
)
        if response.data:
            # print("response.data = ",response.data[0]["original_url"])
            return HttpResponseRedirect(redirect_to=response.data[0]["original_url"])
            # return Response({"message":"successfully retrieved","data":response.data},status=status.HTTP_200_OK)
        else:
            return Response({"message":"code doesn't exist"},status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
