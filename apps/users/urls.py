from django.urls import path, re_path

from apps.users.views import (
    LoginView,
    RegisterView,
    LogoutView,
    CreateListVerseView,
)


urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    re_path(r'^$', CreateListVerseView.as_view(), name='control_panel'),
]
