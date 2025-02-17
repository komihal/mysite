# pages/urls.py
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home_view, name='home'),
    path('projects/', views.projects_view, name='projects'),

    # Отдельные разделы для категорий
    path('projects/category/<str:category>/', views.projects_by_category_view, name='projects_by_category'),

    # Резюме
    path('resume/', views.resume_view, name='resume'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)