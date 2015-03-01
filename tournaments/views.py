from django.core.urlresolvers import reverse_lazy
from django.utils import timezone
from django.views.generic import TemplateView, CreateView

from .forms import TournamentSubmissionForm
from .models import Tournament


class TournamentList(TemplateView):
    template_name = 'tournaments/tournament_list.html'

    def get_tournaments(self):
        return Tournament.objects.filter(
            end_date__gte=timezone.now().date,
            approved=True,
        ).select_related(
            'organising_club',
            'organising_county',
            'venue',
        ).prefetch_related('rounds').order_by(
            'start_date',
            'end_date',
        )

    def get_context_data(self, **kwargs):
        return {
            'tournaments': self.get_tournaments(),
        }


class TournamentSubmit(CreateView):
    template_name = 'tournaments/tournament_submit.html'
    form_class = TournamentSubmissionForm
    success_url = reverse_lazy('tournament-list')
