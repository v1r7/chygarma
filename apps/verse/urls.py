from django.urls import path

from apps.verse.views import IndexView, AuthorDetailView, VerseListView, AuthorlistView, AsyncVerseSearchListView, \
    AsyncAuthorSearchListView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('', VerseListView.as_view(), name="verse_list"),
    path('control_panel/', VerseListView.as_view(), name="verses_list"),
    path('author_detail/<int:pk>', AuthorDetailView.as_view(), name="author_detail"),
    path('authors_list/', AuthorlistView.as_view(), name="author_list"),
    path('search_list/', AsyncVerseSearchListView.as_view(), name='search_list'),
    path('author_search_list/', AsyncAuthorSearchListView.as_view(), name='author_search_list'),
    # path('', CategoryListView.as_view(), name='category_list')
]