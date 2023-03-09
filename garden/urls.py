from django.urls import path
from . import views

urlpatterns = [
    path('garden/', views.GardenList.as_view(), name='garden'),
    path('garden/create/', views.GardenCreate.as_view(), name='garden-create'),
    path('garden/<int:pk>/', views.GardenDetail.as_view(), name='garden-detail'),
    path('ward/', views.WardList.as_view(), name='ward'),
    path('ward/create/', views.WardCreate.as_view(), name='ward-create'),
    path('ward/<int:pk>/', views.WardDetail.as_view(), name='ward-detail'),
    path('ratings/<int:garden_id>/', views.RatingTotal.as_view(), name='ratings'),
    path('ratings/list/<int:garden_id>/', views.RatingList.as_view(), name='ratings-list'),
]
