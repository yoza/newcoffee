"""
simple test
"""

from django.test import TestCase
from django.utils import timezone
import forms
from .models import Trip


class DepatrureFormTest(TestCase):
    """
    test depatrure form
    """
    def setUp(self):
        """
        create trip
        """
        self.trip = Trip.objects.create(name='Trip test',
                                        slug='trip-test')

    def test_departure_form(self):
        """
        Test ``DepartureInlineForm``
        """

        form = forms.DepartureInlineForm(data={'trip': self.trip.id,
                                               'start_date': timezone.now()})

        self.assertEqual(form.is_valid(), True)
