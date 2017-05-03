from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Contest, Work


# Create your views here.
def contest_page(request, year, month, day, id):
        contest = Contest.objects.get(id=id)
        get_in_c = False
        for i in contest.contestants.all():
            if request.user == i:
                get_in_c = True

        contestants = []
        for i in contest.contestants.all():
            contestants.append(i)

        uploaded = False
        for i in contest.works.all():
            if i.author == request.user:
                uploaded = True
                public_md = i.public

        return render(request, 'contest/contest.html', {'contest': contest, 'get_in_c': get_in_c,
                                                        'contestants': contestants, 'uploaded': uploaded,
                                                        'public_md': public_md, })

def edit_work_page(request, year, month, day, id):
    if request.user.is_authenticated():
        contest = Contest.objects.get(id=id)
        uploaded = False
        for i in contest.works.all():
            if i.author == request.user:
                uploaded = True
    else:
        return redirect('/accounts/login/')

    return render(request, 'contest/edit_work.html', {'contest': contest, 'uploaded': uploaded, })


def public_work(request, id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            contest = Contest.objects.get(id=id)
            work = Work(title=request.POST['title'], author=request.user, text_work=request.POST['text_work'], public=None)
            work.save()
            contest.works.add(work)
            return redirect(request.META['HTTP_REFERER'])


def delete_work(request, id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            contest = Contest.objects.get(id=id)
            for i in contest.works.all():
                if i.author == request.user:
                    i.delete()
            return redirect(request.META['HTTP_REFERER'])


def get_in_contest(request, id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            contest = Contest.objects.get(id=id)
            contest.contestants.add(request.user)
            return redirect(reverse('edit_work_page', args=[contest.startDate.year, contest.startDate.month, contest.startDate.day, contest.id]))


def leave_contest(request, id):
    if request.user.is_authenticated():
        if request.method == 'POST':
            contest = Contest.objects.get(id=id)
            contest.contestants.remove(request.user)
            if contest.works.count() != 0:
                i = contest.works.get(author=request.user)
                i.delete()
            return redirect(request.META['HTTP_REFERER'])