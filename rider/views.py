from django.shortcuts import render
from django.views import View


# Create your views here.
class Index(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'rider/index.html')


class About(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'rider/about.html')