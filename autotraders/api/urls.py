from django.urls import path
from . import views

urlpatterns = [
    path('bids/', views.bids, name='bids'),
    path('bidders/', views.bidders, name='bidders'),
    path('copart/', views.copart_accounts, name='copart_accounts'),
]