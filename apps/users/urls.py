from django.urls import path

from apps.users.views import LoginView, RegisterView, LogoutView, ControlPanelListView

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(), name='login'),
    path(r'^$', ControlPanelListView.as_view(), name='control_panel')

]
