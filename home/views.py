from django.shortcuts import render
from .models import Text, Image

# Create your views here.
def Message(request):
    if request.method == 'POST':
        if request.POST.get('text'):
            saveText = Text()
            saveText.text = request.POST.get('text')
            saveText.save()
            return render(request,'message.html')
        if request.POST.get('photo'):
            saveImage = Image()
            saveImage.photo = request.POST.get('photo')
            saveImage.save()
            return render(request,'message.html')
    else:
        return render(request,'message.html')
        