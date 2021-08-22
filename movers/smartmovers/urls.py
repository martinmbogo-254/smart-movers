from django.urls import path
from . import views
from .views import movers_list, homepage,PostCreateView,PostDeleteView,PostUpdateView ,Rate,PostDetail

urlpatterns = [
    path('',views.homepage, name='homepage' ),
    path('post/movers',views.movers_list, name='movers' ),
    # path('post/movers',PostListView.as_view(), name='movers' ),
    path('post/new', PostCreateView.as_view(), name='new_post'),
    path('post/<int:pk>/',views.PostDetail, name='detail' ),
    # path('post/<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='delete'),
     path('post/<int:pk>/rate',views.Rate, name='rate' ),
]
