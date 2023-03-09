from django.urls import path
from .views import PostList, PostDetail, PostCommentList, PostCommentDetail, PostLikeList, PostLikeDetail, PostCreate, PostCommentCreate, PostLikeCreate, PostLikeCount


urlpatterns = [
    path('post/', PostList.as_view(), name='Post'),
    path('post/create/', PostCreate.as_view(), name='PostCreate'),
    path('post/<int:pk>/', PostDetail.as_view(), name='PostDetail'),
    path('post/comment/create/', PostCommentCreate.as_view(), name='PostCommentCreate'),
    path('post/comment/', PostCommentList.as_view(), name='PostComment'),
    path('post/comment/<int:pk>/', PostCommentDetail.as_view(), name='PostCommentDetail'),
    path('post/like/create/', PostLikeCreate.as_view(), name='PostLikeCreate'),
    path('post/like/', PostLikeList.as_view(), name='PostLike'),
    path('post/like/<int:pk>/', PostLikeCount.as_view(), name='PostLikeDetail'),
]