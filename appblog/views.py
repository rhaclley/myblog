from django.shortcuts import render

# Create your views here.

posts = [
    {
        'author': 'Rhaclley',
        'tittle': 'Post 1',
        'content': 'First Post Content',
        'date_posted': 'January 10, 2024'
    }
    {
        'author': 'User',
        'tittle': 'Post 2',
        'content': 'Second Post Content',
        'date_posted': 'December 10, 2023'
    }
]

def home(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

