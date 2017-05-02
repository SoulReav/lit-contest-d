from django.shortcuts import render, HttpResponse, redirect
from .models import Contest


# Create your views here.
def contest_page(request, year, month, day, id):
    if not request.user.is_authenticated() is None:
        contest = Contest.objects.get(id=id)
        return render(request, 'contest/contest.html', {'contest': contest, })
