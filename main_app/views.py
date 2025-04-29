from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def typeface_index(request):
    return render(request, 'typefaces/index.html', {'typefaces': typefaces})


class Typeface:
    def __init__(self, name, designer, classification, image, link):
        self.name = name
        self.designer = designer
        self.classification = classification
        self.image = image
        self.link = link

typefaces = [
    Typeface('Helvetica', 'Sammy Mark', 'Sans Serif', 'Helvetica.png', 'https://example.com/Helvetica'),
    Typeface('GESS', 'Steve Mark', 'Sans Serif', 'GESS.png', 'https://example.com/GESS'),
    Typeface('Futura', 'Donald Alex', 'Sans Serif', 'Futura.png', 'https://example.com/Futura'),
    Typeface('Proxima Nova', 'Lexy Hamilton', 'Sans Serif', 'Proxima.png', 'https://example.com/Proxima')
]