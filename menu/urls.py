from django.urls import path
from .views import Index
from django.conf import settings
from django.conf.urls.static import static

app_name = 'stripePage'
urlpatterns = [
    path('', Index.as_view(), name='index_view'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)