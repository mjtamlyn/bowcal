from django.core.urlresolvers import reverse

import pytest


@pytest.mark.django_db
class TestTournamentList:
    def test_simple(self, client):
        url = reverse('tournament-list')
        response = client.get(url)
        assert response.status_code == 200
