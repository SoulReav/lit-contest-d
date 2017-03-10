from django.http import HttpResponseRedirect
from .models import SiteComments


def post(request):
    comment = SiteComments()
    comment.user = request.user
    comment.comment = request.POST['comment-text']
    comment.url = request.POST['url_page']
    comment.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
