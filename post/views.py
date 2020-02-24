from django.shortcuts import render,redirect,get_object_or_404
from .models import Post

# Create your views here.
def home(req):
    allpost=Post.objects.all()
    return render(req,'home.html',{'posts':allpost})

def new(req):
    return render(req,'new.html')

def create(req):
    onepost=Post()
    onepost.title=req.POST['title']
    onepost.content=req.POST['content']
    onepost.save()
    return redirect('/')

def detail(req,post_id):
    thepost=get_object_or_404(Post,id=post_id)
    return render(req,'detail.html',{'thepost':thepost})

def delete(req,post_id):
    thepost=get_object_or_404(Post,id=post_id)
    thepost.delete()
    return redirect('/')

def edit(req,post_id):
    thepost=get_object_or_404(Post,id=post_id)
    return render(req,'edit.html',{'thepost':thepost})

def update(req,post_id):
    thepost=get_object_or_404(Post,id=post_id)
    thepost.title=req.POST['title']
    thepost.content=req.POST['content']
    thepost.save()
    return redirect('/detail/'+str(post_id))

def search(request):
    word=request.POST['word']
    result=Post.objects.filter(title__icontains=word)
    return render(request,'search.html',{'result':result})