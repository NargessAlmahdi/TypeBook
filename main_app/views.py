from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Typeface
from .forms import RateForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def typeface_index(request):
    typefaces = Typeface.objects.all()
    return render(request, 'typefaces/index.html', {'typefaces': typefaces})

def typeface_detail(request, typeface_id):
    typeface = Typeface.objects.get(id=typeface_id)
    rate_form = RateForm()
    return render(request, 'typefaces/detail.html', {
        'typeface': typeface,
        'rate_form': rate_form
    })

def add_rate(request, typeface_id):
    form = RateForm(request.POST)
    if form.is_valid():
        new_rate = form.save(commit=False)
        new_rate.typeface_id = typeface_id
        new_rate.save()
    return redirect('typeface-detail', typeface_id=typeface_id)


class TypefaceCreate(CreateView):
    model = Typeface
    fields = '__all__'

class TypefaceUpdate(UpdateView):
    model = Typeface
    fields = [ 'name', 'designer', 'classification', 'image', 'link']

class TypefaceDelete(DeleteView):
    model = Typeface
    success_url = '/typefaces/'




# class Typeface:
#     def __init__(self, name, designer, classification, image, link):
#         self.name = name
#         self.designer = designer
#         self.classification = classification
#         self.image = image
#         self.link = link

# typefaces = [
#     Typeface('Helvetica', 'Sammy Mark', 'Sans Serif', 'Helvetica.png', 'https://example.com/Helvetica'),
#     Typeface('GESS', 'Steve Mark', 'Sans Serif', 'GESS.png', 'https://example.com/GESS'),
#     Typeface('Futura', 'Donald Alex', 'Sans Serif', 'Futura.png', 'https://example.com/Futura'),
#     Typeface('Proxima Nova', 'Lexy Hamilton', 'Sans Serif', 'Proxima.png', 'https://example.com/Proxima')
# ]