from django.conf import settings
from django.shortcuts import render_to_response
from django.views.static import serve


def index(request):
    templates = 'chatbot/index.html'
    context = {}
    return render_to_response(templates,context)