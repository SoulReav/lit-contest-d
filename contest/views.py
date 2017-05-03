from django.shortcuts import render, HttpResponse, redirect
from .models import Contest, Work


# Create your views here.
def contest_page(request, year, month, day, id):

    if not request.user.is_authenticated() is None:
        contest = Contest.objects.get(id=id)
        return render(request, 'contest/contest.html', {'contest': contest, })


def edit_work_page(request, year, month, day, id):
    if not request.user.is_authenticated() is None:
        contest = Contest.objects.get(id=id)


    return render(request, 'contest/edit_work.html', {'contest': contest, })

def public_work(request, id):
    if request.method == 'POST':
        contest = Contest.objects.get(id=id)
        work = Work(title=request.POST['title'], author=request.user, text_work=request.POST['text_work'], public=True)
        work.save()
        contest.works.add(work)
        return redirect(request.META['HTTP_REFERER'])
