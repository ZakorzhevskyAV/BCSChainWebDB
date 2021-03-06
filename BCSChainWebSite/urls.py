from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('blocks/<int:block_height>', views.block_page, name='block_page'),
    path('start_background', views.start_background, name='start_background'),
]
