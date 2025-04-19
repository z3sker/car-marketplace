from django.urls import path
from .views import (
    secret_view,
    brand_list,
    CarListCreateView,
    AdListCreateView,
)

urlpatterns = [
    path('secret/', secret_view, name='secret'),
]

urlpatterns += [
    path('brands/', brand_list, name='brand-list'),          # FBV
    path('ads/', AdListCreateView.as_view(), name='ad-list'), # CBV
    path('cars/', CarListCreateView.as_view(), name='car-list-create'),
]