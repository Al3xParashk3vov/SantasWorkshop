from django.urls import path

from SantasWorkshop.base.views import index

# from SantasWorkshop.base.views import HomeView

urlpatterns = [
# path('', HomeView.as_view(), name='home'),
    path('', index, name='index'),

]
