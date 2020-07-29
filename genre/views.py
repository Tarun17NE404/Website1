from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Piece
from django.views import generic


class index(generic.ListView):
    template_name='genre/genretemplate.html'
    def get_queryset(self):
        return Collection.objects.all()


class details(generic.DetailView):
    model=Collection
    template_name='genre/detailtemplate.html'