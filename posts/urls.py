from django.urls import path


from .views import PostList, PostCreate, PostDetail


urlpatterns = [
	path('', PostList.as_view(), name='post_list'),
	path('post/new/', PostCreate.as_view(), name='post_create'),
	path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),

]