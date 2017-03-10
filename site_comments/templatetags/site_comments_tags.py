from django import template
from ..models import SiteComments

register = template.Library()


@register.inclusion_tag('site_comments.html', takes_context=True)
def show_site_comments(context):
    comments = SiteComments.objects.order_by('dateCreated').filter(url=context['request'].get_full_path()).all()
    return {'STATIC_URL': context['STATIC_URL'], 'comments': comments, 'user': context['user'], 'url': context['request'].get_full_path()}