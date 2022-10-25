from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
import qrcode
import os

def QrGeneratorView(request):
    return render(request , 'qrcode.html', {})
   

def generateQr(request):
    qr = qrcode.make(request.POST['noss'])
    qr.save('QrCode\static\qr1.jpg')
    return redirect('qrcode')