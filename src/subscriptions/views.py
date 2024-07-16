from django.views import generic

from .models import Subscription


class SubscriptionListView(generic.ListView):
    template_name = 'subscriptions/list.html'
    queryset = Subscription.objects.all().order_by('id')

subscriptionListView = SubscriptionListView.as_view()

class SubscriptionDetailView(generic.DetailView):
    template_name = 'subscriptions/detail.html'
    queryset = Subscription.objects.all()

subscriptionDetailView = SubscriptionDetailView.as_view()