from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from .models import Contest, Work, Vote
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User


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
        works = contest.works.filter(public=True)
        works = works.exclude(author=request.user)
        table_works = contest.works.filter(public=True)
        public_md = None

        for i in contest.works.all():
            if i.author == request.user:
                uploaded = True
                public_md = i.public

            else:
                public_md = 'NotParticipate'

        error = None
        try:
            vote = Vote.objects.get(author=request.user, contest=contest)
        except ObjectDoesNotExist:
            vote = None

        if request.method == 'POST':
            points = 0
            max_points = 0

            try:
                vote = contest.votes.get(author=request.user)
            except ObjectDoesNotExist:
                for i, work in enumerate(works.all()):
                    points += int(request.POST['select_points_' + str(i+1)])
                    max_points += i+1
                if points != max_points:
                    error = 'VoteIncorrect'
                else:
                    error = None

                    for i, work in enumerate(works.all()):
                        work.raiting_work += int(request.POST['select_points_' + str(i+1)])
                        work.save()
                    vote = Vote(author=request.user, voted=True, )
                    vote.save()
                    contest.votes.add(vote)

        return render(request, 'contest/contest.html', {'contest': contest, 'get_in_c': get_in_c,
                                                        'contestants': contestants, 'uploaded': uploaded,
                                                        'public_md': public_md,
                                                        'works': works,
                                                        'error': error,
                                                        'vote': vote,
                                                        'table_works': table_works, })

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

def cut(s):
    step = 550
    return [s[i:i + step] for i in range(0, len(s), step)]


def read_work_page(request, author, id):
    user = User.objects.get(username=author)
    work = Work.objects.get(author=user, id=id)
    text_work = cut(work.text_work)

    return render(request, 'contest/read_work.html', {'work': work, 'text_work': text_work, })


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