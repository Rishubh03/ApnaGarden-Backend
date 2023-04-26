from django.urls import path
from .views import *


urlpatterns = [
    path('list/', PostList.as_view(), name='Post'),
    path('create/', PostCreate.as_view(), name='PostCreate'),
    path('detail/<int:pk>/', PostDetail.as_view(), name='PostDetail'),
    path('comment/create/', PostCommentCreate.as_view(), name='PostCommentCreate'),
    path('comment/<int:fk>/', PostCommentList.as_view(), name='PostComment'),
    path('comment/detail/<int:pk>/', PostCommentDetail.as_view(), name='PostCommentDetail'),
    path('like/create/', PostLikeCreate.as_view(), name='PostLikeCreate'),
    path('like/', PostLikeList.as_view(), name='PostLike'),
    path('like/<int:pk>/', PostLikeCount.as_view(), name='PostLikeDetail'),
]