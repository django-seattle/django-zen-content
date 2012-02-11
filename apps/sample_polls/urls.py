# Polls Application URLS
# ----------------------
#
# <strong>urls.py</strong>

from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from apps.sample_polls.models import Poll

urlpatterns = patterns('',
    url(r'^$',
        # Use the ListView to display a list of available polls.
        ListView.as_view(
            # Slice the queryset to only display the five most recent polls.
            queryset=Poll.objects.order_by('-pub_date')[:5],
            context_object_name='latest_poll_list',
            template_name='polls/index.html')),
    url(r'^(?P<pk>\d+)/$',
        # Use the DetailView generic view to display the poll as a form.
        DetailView.as_view(
            model=Poll,
            template_name='polls/detail.html')),
    url(r'^(?P<pk>\d+)/results/$',
        # Use the DetailView generic view to display the results.
        # The vote view redirects to this view after accepting a vote.
        DetailView.as_view(
            model=Poll,
            template_name='polls/results.html'),
        # Add a name parameter to facilitate reverse lookups.
        name='poll_results'),
    # The vote view cannot be handled using the basic generic views,
    # so is defined as a separate function-based view.
    url(r'^(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),
)