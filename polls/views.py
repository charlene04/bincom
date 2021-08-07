from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import *
import json
# Create your views here.

def polls(request):
    unit_id = []
    res = Announced_pu_results.objects.all().order_by('polling_unit_id')
    for item in res:
        if item.polling_unit_id not in unit_id:
            unit_id.append(item.polling_unit_id)
            
    context = {'unit_id': unit_id, 'result':res}
    return render(request, "home.html", context)


def lga(request):
    lgas = Lga.objects.all()
    lga_ids = []
    results = []
    for lga in lgas:
        lga_ids.append(lga.lga_id)
    
    for id in lga_ids:
        res = list(Announced_pu_results.objects.filter(polling_unit__lga_id = id).values())
        if len(res) > 0:
            results.append(list(res))
        # for entries in results:
        #     for entry in entries:
        #         if 
    return render(request, "summation.html", {'lgas':lgas})


def lga_selected(request, id):
    results = {}
    res = list(Announced_pu_results.objects.filter(polling_unit__lga_id = id).values())
    for item in res:
        if item["party_abbreviation"] not in results:
            results[item["party_abbreviation"]] = item["party_score"]
        else:
            results[item["party_abbreviation"]] += item["party_score"]
    return JsonResponse(results)


def new_entry(request):
    if request.method == "GET":
        res = Party.objects.all()
        return render(request,'new_entry.html', {'results':res})
    # results = {}
    # res = list(Announced_pu_results.objects.filter(polling_unit__lga_id = id).values())
    # for item in res:
    #     if item["party_abbreviation"] not in results:
    #         results[item["party_abbreviation"]] = item["party_score"]
    #     else:
    #         results[item["party_abbreviation"]] += item["party_score"]
    # return JsonResponse(results)