from django.urls import include, path
from commonuser.views import (CommonUserSignupView,)

app_name ='commonuser'
urlpatterns = [
    path('signup/', CommonUserSignupView, name='signup'),
]
