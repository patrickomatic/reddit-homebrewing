from django.conf.urls import patterns

urlpatterns = patterns('homebrewit.related.views',
    (r'^$', 'view_related'),
)
