from django.shortcuts import render
from django.views.generic import ListView
from .models import Mobile
from django.db.models import Q


# Create your views here.
class MobileListView(ListView):
    model = Mobile
    template_name = "list.html"


class SearchResultsListView(ListView):
    model = Mobile
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Mobile.objects.filter(
            Q(name__icontains=query) | Q(manufacturer__icontains=query)
        )
