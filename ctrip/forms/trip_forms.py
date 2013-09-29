"""
trip forms

"""
from __future__ import absolute_import

from django import forms
from django.utils.translation import ugettext_lazy as _

from django.forms import Form
from datetime import date
from django.forms.extras.widgets import SelectDateWidget

from django.utils.text import slugify

from ctrip.models import Trip, Departure


def validate_date(value):
    """
    validate date
    """
    if value < date.today():
        err_text = _(u'Date must not be less than today.')
        raise forms.ValidationError(err_text)


class DepartureInlineForm(forms.ModelForm):
    """
    inline form for input departure
    """
    datewidget = \
        SelectDateWidget(years=range(date.today().year, date.today().year+2))
    start_date = \
        forms.DateField(validators=[validate_date],
                        required=True,
                        widget=datewidget)

    def __init__(self, *args, **kwargs):
        super(DepartureInlineForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Departure


class TripForm(Form):
    """
    form for input trip
    """
    name = forms.CharField(max_length=255,
                           widget=
                           forms.TextInput(attrs={'class': 'required',
                                                  'placeholder': _('Name *')}))

    slug = forms.CharField(widget=forms.HiddenInput(attrs={}), required=False)

    class Meta:
        model = Trip

    def __init__(self, request=None, data=None, instance=None,
                 *args, **kwargs):
        """
        initial trip form
        """
        self.request = request
        if request is None:
            raise TypeError("Keyword argument 'request' must be supplied")
        kwargs['initial'] = instance.__dict__

        super(TripForm, self).__init__(data=data, *args, **kwargs)

    def clean(self):
        """
        Returns the dict of data to be used to create a trip
        """
        name = self.cleaned_data.get('name', None)
        slug = slugify(name)

        return dict(name=name, slug=slug)
