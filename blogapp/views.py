from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Blog
from .forms import BlogPost
# Create your views here.

def home(request):
    blogs = Blog.objects
    blog_list=Blog.objects.all()
    paginator = Paginator(blog_list,3)
    total_len=len(blog_list)
    
    page = request.GET.get('page',1)
    posts = paginator.get_page(page)
    
    
    try:
        lines = paginator.page(page) 
    except PageNotAnInteger: 
        lines = paginator.page(1) 
    except EmptyPage: 
        lines = paginator.page(paginator.num_pages) 
        
    index = lines.number -1 
    max_index = len(paginator.page_range) 
    start_index = index -2 if index >= 2 else 0 
    if index < 2 : 
        end_index = 5-start_index
    else : 
        end_index = index+3 if index <= max_index - 3 else max_index 
    page_range = list(paginator.page_range[start_index:end_index]) 
    
    context = { 'blogs':blogs,'blog_list': lines , 'posts':posts, 'page_range':page_range, 'total_len':total_len, 'max_index':max_index-2 } 
    return render (request,'blogapp/home.html', context )


def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blogapp/detail.html', {'blog': blog_detail})




def new(request):
    if request.method =='POST':
        form = BlogPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date=timezone.now()
            post.save()
            return redirect('home')
    else:
        form = BlogPost()
        return render(request,'blogapp/new.html',{'form':form})
    