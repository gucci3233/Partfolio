from django.urls import path

from apps.views import indexListView, AboutListView, PortfolioListView, ContactListView

urlpatterns = [
    path('', indexListView.as_view(), name='index'),
    path('about/', AboutListView.as_view(), name='about'),
    path('portfolio', PortfolioListView.as_view(), name='portfolio'),
    path('contact', ContactListView.as_view(), name='contact'),
]
