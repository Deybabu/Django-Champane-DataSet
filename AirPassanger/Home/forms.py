from django import forms
from .models import DateRange


class DateRangeForm(forms.ModelForm):
    class Meta:
        model = DateRange
        fields = ['start_date', 'end_date']