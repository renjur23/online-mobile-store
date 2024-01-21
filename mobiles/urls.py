from django.urls import path
from .views import MobileListView, SearchResultsListView


urlpatterns = [
    path("", MobileListView.as_view(), name="list"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
