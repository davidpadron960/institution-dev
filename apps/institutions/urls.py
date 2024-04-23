from django.urls import path
from apps.institutions.views.views import institution_list,institution_detail

urlpatterns = [
    path('institution/',institution_list,name='institution_list'),
    path('institution/<int:pk>/',institution_detail,name='institution_detail_view'),
]