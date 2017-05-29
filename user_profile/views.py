from django.shortcuts import render, HttpResponse, redirect
from avatar.views import _get_avatars
from avatar.views import add
from avatar.models import Avatar
from .models import UserProfile

# Create your views here.


def show_profile(request):
    if not request.user.is_authenticated() is None:
        user = UserProfile.objects.get(user=request.user)
        full_name = user.first_name + ' ' + user.last_name + ' '
        avatar, avatars = _get_avatars(request.user)
        context = {
            'avatar': avatar,
            'avatars': avatars,
            'full_name': full_name, }
        return render(request, 'user_profile/profile.html', context)
    else:
        redirect('/accounts/login/')


def upload_avatar(request):
    if not request.user.is_authenticated() is None:
        avatar, avatars = _get_avatars(request.user)
        context = {
            'avatar': avatar,
            'avatars': avatars, }
    if request.method == 'POST':
        if not avatar is None:
            Avatar.objects.filter(id__in=[avatar.id]).delete()
        return add(request)
    else:
        return HttpResponse('404')


def edit_name(request):
    context = {}
    if not request.user is None:
        full_name = request.user.first_name + ' ' + request.user.last_name
        avatar, avatars = _get_avatars(request.user)
        context = {
            'avatar': avatar,
            'avatars': avatars,
            'full_name:': full_name, }

        if request.method == 'POST':

            user = UserProfile.objects.get(user=request.user)
            if not request.POST['first_name'] is None:

                user.first_name = request.POST['first_name']
            if not request.POST['last_name'] is None:

                user.last_name = request.POST['last_name']
            user.save()

            context['full_name'] = full_name

            return redirect('/accounts/profile/', context)

    return render(request, 'user_profile/edit_name.html', context)
