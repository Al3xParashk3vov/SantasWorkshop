from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, FormView

from SantasWorkshop.presents.models import Present


# Create your views here.
# class HomeView(TemplateView):
#     template_name = 'common/index.html'

def index(request):
    return render(request, 'common/index.html')


class DashboardView(ListView):
    template_name = 'presents/dashboard.html'
    context_object_name = 'presents'
    paginate_by = 5

    def get_queryset(self):
        queryset = Present.objects.all()

        if 'query' in self.request.GET:
            query = self.request.GET.get('query')
            queryset = queryset.filter(name__icontains=query)

        return queryset

def about(request):
    return render(request, 'common/about.html')

def story(request):
    return render(request, 'common/story.html')

def custom_404_view(request, exception):
    return render(request, 'common/404.html', status=404)
