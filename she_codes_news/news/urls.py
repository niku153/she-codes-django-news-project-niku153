from django.urls import path
from . import views
from .views import CategoryView

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.StoryView.as_view(), name='story'),
    path('add-story/', views.AddStoryView.as_view(),name='newStory'),
    path('add-category/', views.AddCategoryView.as_view(),name='addCategory'),
    path('<int:pk>/edit', views.EditStoryView.as_view(), name='editStory'),
    path('<int:pk>/delete', views.DeleteStoryView.as_view(), name='deleteStory'),
    path('<int:pk>/comment', views.AddCommentView.as_view(),name='addComment'),
    path('category/<str:cats>/', CategoryView, name='category')
]
