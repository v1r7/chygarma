from django.urls import path

from apps.verse.views import IndexView, AuthorListView, VerseListView, AuthorsView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('', VerseListView.as_view(), name="verse_list"),
    path('authors_page/', AuthorListView.as_view(), name="authors_page"),
    path('authors_profile/', AuthorsView.as_view(), name='authours_profile')

]