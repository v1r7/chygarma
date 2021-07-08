from django.urls import path

from apps.verse.views import MainView

urlpatterns = [
    path('', MainView.as_view(), name='main_page'),

    # path('authors/', AuthorsView.as_view(), name='author_page'),
    # path('works/', VerseView.as_view(), name='works_page'),
    # path('desktop/', DesktopView.as_view(), name='desktop_view')


]