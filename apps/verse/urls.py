from django.urls import path

from apps.verse.views import IndexView, VerseListView, AuthorDetailView, AuthorlistView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('', VerseListView.as_view(), name="verse_list"),
    path('control_panel/', VerseListView.as_view(), name="verses_list"),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name="author_detail"),
    path('authors_list/', AuthorlistView.as_view(), name="author_list")

]