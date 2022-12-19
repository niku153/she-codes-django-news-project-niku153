from django.urls import path
from . import views
from .views import CategoryView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('favourite/', views.favourite_post_list, name='favourite_post_list'),
    path('add-category/', views.AddCategoryView.as_view(),name='addCategory'),
    path('<int:pk>/edit', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('<int:pk>/comment', views.AddCommentView.as_view(),name='addComment'),
    path('category/<str:cats>/', CategoryView, name='category'),
    path('<int:pk>/like', views.like_post, name='like'),
    path('<int:pk>/favourite_post', views.favourite_post, name='favourite_post'),

]
