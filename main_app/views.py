from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Typeface, Rating, Note
from .forms import RatingForm, NoteForm
from .models import Pairing
from django.views.generic import ListView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin



def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def typeface_index(request):
    typefaces = Typeface.objects.filter(user=request.user)
    return render(request, 'typefaces/index.html', {'typefaces': typefaces})


def typeface_detail(request, typeface_id):
    typeface = Typeface.objects.get(id=typeface_id)
    note_form = NoteForm()
    user_rating = None
    rating_form = RatingForm()

    pairings = Pairing.objects.exclude(id__in=typeface.pairings.all().values_list('id', flat=True))

    if request.user.is_authenticated:
        user_rating = typeface.rating_set.filter(user=request.user).first()
        if user_rating:
            rating_form = RatingForm(initial={'rating': user_rating.rating})

    return render(request, 'typefaces/detail.html', {
        'typeface': typeface,
        'rating_form': rating_form,
        'note_form': note_form,
        'user_rating': user_rating,
        'pairings': pairings,
    })

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

def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id)
    if note.user == request.user:
        typeface_id = note.typeface.id
        note.delete()
        return redirect('typeface-detail', typeface_id=typeface_id)
    return redirect('typeface-detail', typeface_id=note.typeface.id)


def assoc_pairing(request, typeface_id, pairing_id):
    Typeface.objects.get(id=typeface_id).pairings.add(pairing_id)
    return redirect('typeface-detail', typeface_id=typeface_id)


def remove_pairing(request, typeface_id, pairing_id):
    typeface = Typeface.objects.get(id=typeface_id)
    typeface.pairings.remove(pairing_id)
    return redirect('typeface-detail', typeface_id=typeface.id)

def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in
            login(request, user)
            return redirect('cat-index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
    # Same as: 
    # return render(
    #     request, 
    #     'signup.html',
    #     {'form': form, 'error_message': error_message}
    # )



class TypefaceCreate(LoginRequiredMixin, CreateView):
    model = Typeface
    fields = ['name', 'designer', 'classification', 'image', 'link']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


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

class Home(LoginView):
    template_name = 'home.html'