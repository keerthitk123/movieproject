from django.http import HttpResponse
from django.shortcuts import render, redirect

from movieapp.forms import MovieForm
from movieapp.models import Movie1


# Create your views here.
def index(request ):
    movie=Movie1.objects.all()
    context = {
        'movie_list':movie
    }
    return render(request,'index.html',context)

def detail(request,movie_id):
    mv1=Movie1.objects.get(id=movie_id)
    return render(request,'detail.html',{'mv1':mv1})

def add_movie(request):
    if request.method=="POST":
        nme=request.POST.get('nme',)
        desc= request.POST.get('desc',)
        year= request.POST.get('year',)
        img =request.FILES.get['img']
        mv2=Movie1(nme=nme,desc=desc,year=year,img=img)
        mv2.save()
        return redirect('/')
    return render(request,'add.html')
def update(request,id):
    movie = Movie1.objects.get(id=id)
    form = MovieForm(request.POST or None, request.FILES, instance=movie)
    if form.is_valid():
        return redirect('/')
    return render(request,'edit.html', {'form': form, 'movie': movie})


def delete(request, id):
    if request.method == 'POST':
        movie = Movie1.objects.get(id=id)
        movie.delete()
        return redirect('/')
    return render(request,'delete.html')



