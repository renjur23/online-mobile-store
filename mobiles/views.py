from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Mobile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q


# Create your views here.
class MobileListView(ListView):
    model = Mobile
    template_name = "list.html"


class MobileDetailView(DetailView):
    model = Mobile
    template_name = "detail.html"


class MobileCheckoutView(LoginRequiredMixin, DetailView):
    model = Mobile
    template_name = "checkout.html"
    login_url = "login"


class SearchResultsListView(ListView):
    model = Mobile
    template_name = "search_results.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        return Mobile.objects.filter(
            Q(name__icontains=query) | Q(manufacturer__icontains=query)
        )
