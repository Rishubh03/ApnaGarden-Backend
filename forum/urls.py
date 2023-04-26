from django.urls import path
from .views import *

urlpatterns = [
	path('list/', ForumView.as_view(),name="Forum List"),
	path('detail/<int:pk>/', ForumDetail.as_view(),name="Forum Detail"),
	path('thread/<int:fk>/', ThreadView.as_view(),name="Thread List"),
	path('thread/detail/<int:pk>/', ThreadDetail.as_view(),name="Thread Detail"),
]