from django.core.urlresolvers import reverse

import pytest

from .models import Tournament


def assert_valid_form_submit(response):
    __tracebackhide__ = True
    if response.status_code == 302:
        return
    elif response.status_code == 200:
        message = 'Form submission not valid: %s' % repr(response.context['form'].errors)
    else:
        message = 'Received status code: %s' % response.status_code
    pytest.fail(message)


@pytest.mark.django_db
class TestTournamentList:
    def test_simple(self, client):
        url = reverse('tournament-list')
        response = client.get(url)
        assert response.status_code == 200


@pytest.mark.django_db
class TestTournamentSubmit:
    def test_get(self, client):
        url = reverse('tournament-submit')
        response = client.get(url)
        assert response.status_code == 200

    def test_post(self, client):
        url = reverse('tournament-submit')
        data = {
            'name': 'foo',
            'shoot_type': 'I',
            'record_status': 'None',
            'start_date': '2015-01-01',
            'end_date': '2015-01-01',
        }
        response = client.post(url, data)
        assert_valid_form_submit(response)
        assert Tournament.objects.count() == 1
        tournament = Tournament.objects.get()
        assert tournament.name == data['name']

    def test_without_end_date(self, client):
        url = reverse('tournament-submit')
        data = {
            'name': 'foo',
            'shoot_type': 'I',
            'record_status': 'None',
            'start_date': '2015-01-01',
            'multi_day_shoot': False,
        }
        response = client.post(url, data)
        assert_valid_form_submit(response)
        assert Tournament.objects.count() == 1
        tournament = Tournament.objects.get()
        assert tournament.start_date == tournament.end_date
