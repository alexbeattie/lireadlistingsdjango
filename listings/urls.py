from django.urls import path

from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.listing_list, name='listing_list'),
    path('<int:listing_id>/', views.listing_detail, name='listing_detail'),
]
