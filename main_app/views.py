from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from .models import Blop

def home(request):
  this is nonsense
  videos = Blop.objects.exclude(video = None)
  pictures = Blop.objects.exclude(image = None)
  articles = Blop.objects.exclude(article = "")
  return render(request, 'main_app/home.html',{'videos': videos,
   'pictures':pictures,
   'articles':articles,
   })

def blop_details(request, blop_id):
  blop = Blop.objects.get(id=blop_id)
  return render(request, 'main_app/detail.html', {
    'title': blop.title,
    'video': blop.video,
    'image': blop.image,
    'article': blop.article,
    'likes': blop.likes,
  })

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('main_app:home')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class BlopCreate(CreateView):
  #add something that checks if a user is logged in.
  #if user is not logged in they are redirected to the login page
  model = Blop
  fields = ['title', 'video', 'image', 'article']
  def form_valid(self, form):
    form.instance.creator = self.request.user
    return super().form_valid(form)