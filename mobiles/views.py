from django.shortcuts import render
from django.views.generic import ListView
from .models import Mobile
from django.db.models import Q


# Create your views here.
class BooksListView(ListView):
    model = Mobile
    template_name = "list.html"
