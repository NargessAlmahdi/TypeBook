from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('typefaces/', views.typeface_index, name='typeface-index'),
  path('typefaces/<int:typeface_id>/', views.typeface_detail, name='typeface-detail'),
  path('typefaces/create/', views.TypefaceCreate.as_view(), name='typeface-create'),
  path('typefaces/<int:pk>/update/', views.TypefaceUpdate.as_view(), name='typeface-update'),
  path('typefaces/<int:pk>/delete/', views.TypefaceDelete.as_view(), name='typeface-delete'),
  path('typefaces/<int:typeface_id>/add-rating-note/', views.add_rating_note, name='add-rating-note'),
  path('notes/<int:note_id>/delete/', views.delete_note, name='delete-note'),
  path('pairings/create/', views.PairingCreate.as_view(), name='pairing-create'),
  path('pairings/<int:pk>/', views.PairingDetail.as_view(), name='pairing-detail'),
  path('pairings/', views.PairingList.as_view(), name='pairing-index'),
  path('pairings/<int:pk>/update/', views.PairingUpdate.as_view(), name='pairing-update'),
  path('pairings/<int:pk>/delete/', views.PairingDelete.as_view(), name='pairing-delete'),
  path('typefaces/<int:typeface_id>/assoc_pairing/<int:pairing_id>/', views.assoc_pairing, name='assoc-pairing'),
  path('typefaces/<int:typeface_id>/remove_pairing/<int:pairing_id>/', views.remove_pairing, name='remove-pairing'),
  path('accounts/signup/', views.signup, name='signup'),
]

