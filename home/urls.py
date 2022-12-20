from django.urls import path
from . import views

urlpatterns = [
    path('', views.homes, name='homes'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('bitcoin', views.bitcoin, name='bitcoin'),
    path('watchlist', views.watchlist, name='watchlist'),
    path('prediction', views.prediction, name='prediction'),
    path('stockmarket', views.stockmarket, name='stockmarket'),
    path('stocknews', views.stocknews, name='stocknews'),
    path('stockprediction', views.stockprediction, name='stockprediction'),
    path('blog', views.blog, name='blog'),
    path('faqask',  views.faqask, name='faqask'),
    path('contact', views.contact, name='contact'),

]
