from django.urls import path
from . import views
from customer_service.views import signup_view



urlpatterns = [
    path('submit/', views.submit_request, name='submit_request'),
    path('track/', views.track_requests, name='track_requests'),
    path('signup/', signup_view, name='signup'),

    path('account/', views.account_info, name='account_info'),
    path('logout/', views.custom_logout, name='logout'),
    path('login/', views.login_view, name='login'),  

]
