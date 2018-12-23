from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [

    #/login/
    path('', views.Login_View.as_view(), name="login"),

    #/inventory/
    path('home/', views.home, name="home"),

    #/search/
    path('search/', views.search, name="search"),

    #/inventory/
    path('groups/', views.IndexView.as_view(), name="index"),

    #/userregistration
    path('register/', views.UserFormView.as_view(), name="register"),

    #/inventory/
    path('devices/', views.DeviceIndex.as_view(), name="device_index"),

    #/inventory/id/
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name="detail"),

    path('devices/<int:pk>/', views.DeviceDetailView.as_view(), name="device_detail"),

    # /inventory/group/create/-----"CREATE VIEW"
    path('group/create/', views.GroupCreate.as_view(), name="create-group"),

    # /inventory/group/create/-----"CREATE VIEW"
    path('device/create/', views.DeviceCreate.as_view(), name="create-device"),

    # /inventory/group/id/-----"UPDATE VIEW"
    path('groups/<int:pk>/update/', views.GroupUpdate.as_view(), name="update-group"),
    path('devices/<int:pk>/update/', views.DeviceUpdate.as_view(), name="update-device"),

    # /inventory/group/id/delete-----"DELETE VIEW"
    path('groups/<int:pk>/delete/', views.GroupDelete.as_view(), name="delete-group"),
    path('devices/<int:pk>/delete/', views.DeviceDelete.as_view(), name="delete-device"),

]