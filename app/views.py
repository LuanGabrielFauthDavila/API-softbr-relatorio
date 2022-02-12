from django.shortcuts import render, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.core.exceptions import ObjectDoesNotExist
from . import models
import json

# Create your views here.
def home(request):
    if request.method == "GET":
        try:
            key = request.GET['key']
            try:
                keys = models.KeysRelatorioFiscal.objects.get(key=key)
                data = str(keys.expiration_date).split(' ').pop(0).split('-')
                d = {
                    "key": keys.key, 
                    "year": data[0],
                    "month": data[1],
                    "day": data[2],
                }
                print(str(keys.expiration_date))
                return HttpResponse(json.dumps(d), status=200, headers={'content-type': 'application/json'})
            except ObjectDoesNotExist as e:
                print(e)
                return HttpResponse(status=404)
        except MultiValueDictKeyError as e:
            print(e)
            return HttpResponse(status=404)
        

    