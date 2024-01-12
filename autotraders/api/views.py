from django.shortcuts import render
from django.http import HttpResponse

def bidders(request):
    print(request)
    return HttpResponse("Bidders")


def bids(request):
    return HttpResponse("Bids")


def copart_accounts(request):
    return HttpResponse("Copart Accounts")