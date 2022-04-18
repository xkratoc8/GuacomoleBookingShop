from django.urls import path
from .views import (ListViewAfter, DetailViewAfter, CreateViewAfter,
                    UpdateView, DeleteViewAfter, UserListView,
                    )
from . import views

urlpatterns = [
    path("about/", views.about, name="about"),
    path("base/", views.base, name="base"),
    path("latest_updates/", views.latest_updates, name="latest_updates"),
    path('', ListViewAfter.as_view(), name='index'),
    path('post/<int:pk>/', DetailViewAfter.as_view(), name='post-detail'),
    path('post/new/', CreateViewAfter.as_view(), name='post-create'),
    path('post/<int:pk>/update/',
         UpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/',
         DeleteViewAfter.as_view(), name='post-delete'),
    path('user/<str:username>',
         UserListView.as_view(), name='user-posts'),

]
