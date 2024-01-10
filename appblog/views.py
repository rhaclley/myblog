from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Rhaclley',
        'title': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 10, 2024'
    },
    {
        'author': 'Rhaclley',
        'title': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December 10, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})

