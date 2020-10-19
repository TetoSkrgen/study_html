from django.shortcuts import render
from django.utils import timezone

from ..models import Post


def home(request):
    return render(request, 'blog/home.html')
