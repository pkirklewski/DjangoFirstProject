from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

def index(request):
    return HttpResponse("This is index")

def get_data(request, *args, **kwargs):
    data = {
            "sales": 100,
            "customers": 10,}
    return JsonResponse(data)
