from django.urls import path

from apps.verse.views import MainView, VerseListView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('', VerseListView.as_view(), name="verse_list"),

    # path('authors/', AuthorsView.as_view(), name='author_page'),
    # path('works/', WorksView.as_view(), name='works'),
    # path('desktop/', DesktopView.as_view(), name='desktop_view')


]