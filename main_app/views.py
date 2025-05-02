from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Typeface, Rating, Note
from .forms import RatingForm, NoteForm
from .models import Pairing
from django.views.generic import ListView, DetailView


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def typeface_index(request):
    typefaces = Typeface.objects.all()
    return render(request, 'typefaces/index.html', {'typefaces': typefaces})

def typeface_detail(request, typeface_id):
    typeface = Typeface.objects.get(id=typeface_id)
    note_form = NoteForm()
    user_rating = None
    rating_form = RatingForm()

    if request.user.is_authenticated:
        user_rating = typeface.rating_set.filter(user=request.user).first()
        if user_rating:
            rating_form = RatingForm(initial={'rating': user_rating.rating})

    return render(request, 'typefaces/detail.html', {
        'typeface': typeface,
        'rating_form': rating_form,
        'note_form': note_form,
        'user_rating': user_rating,
    })

@login_required
def add_rating_note(request, typeface_id):
    if request.method == 'POST':
        rating_value = request.POST.get('rating')
        note_text = request.POST.get('note')
        typeface = get_object_or_404(Typeface, id=typeface_id)

        if rating_value:
            Rating.objects.update_or_create(
                user=request.user,
                typeface=typeface,
                defaults={'rating': rating_value}
            )

        if note_text.strip():
            Note.objects.create(
                user=request.user,
                typeface=typeface,
                note=note_text
            )

        return redirect('typeface-detail', typeface_id=typeface_id)

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user == request.user:
        typeface_id = note.typeface.id
        note.delete()
        return redirect('typeface-detail', typeface_id=typeface_id)
    return redirect('typeface-detail', typeface_id=note.typeface.id)



class TypefaceCreate(CreateView):
    model = Typeface
    fields = '__all__'

class TypefaceUpdate(UpdateView):
    model = Typeface
    fields = ['name', 'designer', 'classification', 'image', 'link']

class TypefaceDelete(DeleteView):
    model = Typeface
    success_url = '/typefaces/'

class PairingCreate(CreateView):
    model = Pairing
    fields = '__all__'

class PairingList(ListView):
    model = Pairing

class PairingDetail(DetailView):
    model = Pairing

class PairingUpdate(UpdateView):
    model = Pairing
    fields = '__all__'

class PairingDelete(DeleteView):
    model = Pairing
    success_url = '/pairings/'