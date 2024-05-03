from django.urls import path

from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbviewhome/',views.listview.as_view(),name='cbviewhome'),
    path('cbviewdetail/<int:pk>/', views.Detailview.as_view(), name='cbviewdetail'),
    path('cbviewupdate/<int:pk>/', views.updateview.as_view(), name='cbviewupdate'),
    path('cbviewdelete/<int:pk>/', views.deleteview.as_view(), name='cbviewdelete'),

]
