from django.conf.urls.defaults import patterns, url
from .utils import route

urlpatterns = patterns('subscription.views',
    url(r'^(\d+)/sucesso/$', 'success', name='success'),
    route(r'^$', GET='new', POST='create', name='subscribe'),
)