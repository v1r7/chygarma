from django.urls import path

from apps.verse.views import IndexView, VerseListView, VerseDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    # path('', VerseListView.as_view(), name="verse_list"),
    # path('control_panel/', VerseListView.as_view(), name="verses_list"),
    path('verse_detail/<int:pk>', VerseDetailView.as_view(), name="verse_detail")

]