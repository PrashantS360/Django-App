from django.shortcuts import render
from blog.models import Blog,Language
# from django.contrib import messages

# Create your views here.
def home(req):
    posts = []
    selected_lang = "en"
    languages = Language.objects.all().values()
    if req.method=="POST":
        selected_lang = req.POST["language"]
    posts = Blog.objects.filter(language_id=selected_lang).values()
    curr_lan = Language.objects.filter(code=selected_lang).values()[0]
    return render(req, 'home.html',{"posts":posts, "languages":languages, "curr_lan":curr_lan})