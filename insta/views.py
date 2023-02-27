from django.shortcuts import render, get_object_or_404, redirect
from .models import Profile, Message, Post

# Create your views here.


def index(request):
    profiles = Profile.objects.all()
    posts = Post.objects.all()

    context = {
        'profiles': profiles,
        'posts': posts,
    }
    return render(request, 'insta/index.html', context)


def like_post(request, post_id):
    post = Post.objects.get(id=post_id)
    # ids are 8 umang, 9 nisha, 10 nisarg
    user = Profile.objects.get(id=8)
    post.like_post(user)
    return redirect('insta:index')


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'insta/profile_list.html', {'profiles': profiles})


def profile(request, user_id):
    # Get the User object from the database based on the user_id parameter
    user = get_object_or_404(Profile, id=user_id)

    # Render the 'profile.html' template with the user object
    return render(request, 'insta/profile.html', {'user': user})

def message(request):
    messages = Message.objects.all()
    return render(request, 'insta/message.html', {'messages': messages})