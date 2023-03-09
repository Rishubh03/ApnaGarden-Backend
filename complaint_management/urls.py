from django.urls import path
from .views import ComplaintList, FeedbackList, ComplaintDetail,CreateComplaint


urlpatterns = [
    path('createcomplaint/', CreateComplaint.as_view(), name='Create Complaint'),
    path('listcomplaint/', ComplaintList.as_view(), name='List Complaint'),
    path('<int:pk>/', ComplaintDetail.as_view(), name='Complaint Details'),
    path('feedback/', FeedbackList.as_view(), name='Feedback'),

]