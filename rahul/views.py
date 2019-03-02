from django.shortcuts import render
import requests
from django.contrib import messages
from django.views import generic
from django.contrib import messages
from django.shortcuts import render
from .forms import SignUpForm,UpdateProfile,BookForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Product,Categoty
import datetime
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.utils import timezone




class BlogCreateView(CreateView):
    model = Product
    template_name = 'Book/addbook.html'
    fields = ['categoty', 'name', 'image','file','description','specification','seller','pub_date','available']
    success_url = '/rahul/new/book/'


# def newbook(request):
#     if request.method == 'POST':
#         form = BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('Book/addbook.html')
#     else:
#         BookForm()
#     return render(request, 'Book/addbook.html', {
#         'form': form
#     })

# def newbook(request):
#     if request.method == "POST":
#         form = BookForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = BookForm()
#     return render(request, 'blog/post_edit.html', {'form': form})


def BlogListView(request):
    time = timezone.now().date()
    contact_list = Product.objects.all()
    search_term=''

    if 'q' in request.GET:
        search_term = request.GET['q']
        contact_list = contact_list.filter(Q(name__icontains=search_term)|
                                           Q(seller__icontains=search_term)).distinct()
        

                        
    page = request.GET.get('page', 1)
    paginator = Paginator(contact_list, 16)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)


    return render(request, 'Book/booklist.html', {'users': users})

class CatCreateView(CreateView):
    model = Categoty
    template_name = 'Book/addcat.html'
    fields = ['name']
    #messages.success('Your request has been submitted, a realtor will get back to you soon')
    success_url = '/rahul/new/cat/'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'Book/bookdetail.html'