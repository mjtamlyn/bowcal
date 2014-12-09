from django.views.generic import TemplateView

from .adapters import tournaments


class TournamentList(TemplateView):
    template_name = 'tournaments/tournament_list.html'

    def get_tournaments(self):
        return tournaments.get_list()

    def get_context_data(self, **kwargs):
        return {
            'tournaments': self.get_tournaments(),
        }
