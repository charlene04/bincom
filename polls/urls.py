from .views import *
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', polls),
    path('stats/', lga),
    path('stats/<int:id>/', lga_selected),
    path('new/', new_entry)
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
