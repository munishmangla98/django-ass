from django.urls import path
from .views import PostList, PostDetail, CommentListCreate, CommentDetail, UserCreate, LogoutView

urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('posts/<int:post_pk>/comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('signup/', UserCreate.as_view(), name='user-create'),
    path('logout/', LogoutView.as_view(), name='logout'),

]
