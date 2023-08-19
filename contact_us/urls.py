from django.urls import path
from . import views


urlpatterns = [
    path('', views.ContactView.as_view(), name='contact_us_page'),
    path('create-profile', views.CreateProfileView.as_view(), name='create_profile_page'),
    path('profile-view', views.ProfileList.as_view(), name='profiles_page')

]
