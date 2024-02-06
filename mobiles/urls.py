from django.urls import path
from .views import (
    MobileListView,
    MobileDetailView,
    MobileCheckoutView,
    SearchResultsListView,
)


urlpatterns = [
    path("", MobileListView.as_view(), name="list"),
    path("<int:pk>/", MobileDetailView.as_view(), name="detail"),
    path("<int:pk>/checkout/", MobileCheckoutView.as_view(), name="checkout"),
    path("search/", SearchResultsListView.as_view(), name="search_results"),
]
