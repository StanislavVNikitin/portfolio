from django.urls import path
from .apps import PortfolioConfig

from .views import *

app_name = PortfolioConfig.name

urlpatterns = [
    path("portfolio/<str:slug>", PortfolioView.as_view(), name="portfolio"),
    path("portfolio", PortfolioListView.as_view(), name="portfoliolist"),
    path("", HomeView.as_view(), name="home"),
]