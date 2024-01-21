from django.urls import path
from .views import BooksListView, SearchResultsListView


urlpatterns = [
    path("", BooksListView.as_view(), name="list"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
