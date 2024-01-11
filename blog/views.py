from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# posts = [
#     {
#         'author':'CoreyMS',
#         'title':'Blog post 1',
#         'content':'First Post Content',
#         'date_posted':'August 27, 2018'
#     },
#     {
#         'author':'Jane Doe',
#         'title':'Blog post 2',
#         'content':'Second Post Content',
#         'date_posted':'August 28, 2018'
#     }
# ]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    return render(request,'blog/home.html',context)

def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    return render(request,'blog/about.html',{'title':'About'})