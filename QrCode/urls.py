from django.urls import path
from .views import QrGeneratorView, generateQr
urlpatterns = [
    path('', QrGeneratorView, name='qrcode'),
    path('generate', generateQr, name='qrcodegen'),
]
