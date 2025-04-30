from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('typefaces/', views.typeface_index, name='typeface-index'),
  path('typefaces/<int:typeface_id>/', views.typeface_detail, name='typeface-detail'),
  path('typefaces/create/', views.TypefaceCreate.as_view(), name='typeface-create'),
  path('typefaces/<int:pk>/update/', views.TypefaceUpdate.as_view(), name='typeface-update'),
  path('typefaces/<int:pk>/delete/', views.TypefaceDelete.as_view(), name='typeface-delete'),
  path('typefaces/<int:typeface_id>/add-rate/', views.add_rate, name='add-rate'),

]

