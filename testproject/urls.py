from django.contrib import admin
from django.urls import path
from articles.views import *
from accountapp.views import *

urlpatterns = [
    path('', home_view),
    path('articles/', article_search_view),
    path('articles/<slug:slug>/', article_detail_view),
    path('articles/create/', article_create_view),
    path('admin/', admin.site.urls),

    path('login/', login_view),
    path('logout/', logout_view),
    path('register/', register_view),
]
