from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.models import Candidate


class ProfilePageView(TemplateView):
    template_name = 'codefundo/profile.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

class VoteHelperPageView(TemplateView):
    template_name = 'codefundo/helper.html'

    def get_context_data(self, **kwargs):
        context = super(VoteHelperPageView, self).get_context_data()
        context['candidates'] = Candidate.objects.all()
        return context


class ThanksView(TemplateView):
    template_name = 'codefundo/thanks.html'


def detail(request, candidate_id):
    return HttpResponse("You're looking at candidate %s." % candidate_id)
