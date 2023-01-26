from django.shortcuts import render
from blog.models import Blog
from django.contrib import messages

# Create your views here.
def home(req):
    if req.method=="POST":
        title = req.POST['title']
        content = req.POST['content']

        if(len(title)<2 or len(content)<11):
            messages.error(req, 'Please fill the form correctly (Minimum length of title and content should be at least 2 and 11 respectively)!')
        else:
            blog = Blog(title=title, content=content)
            blog.save()
            messages.success(req, 'Your blog has been posted suffessfully!')
    return render(req, 'home.html')