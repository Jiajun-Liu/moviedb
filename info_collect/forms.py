from dal import autocomplete
from django import forms
from .models import *
from dal_select2.widgets import ModelSelect2, ModelSelect2Multiple, Select2Multiple, Select2


class ProducerMovieDutyForm(forms.ModelForm):
    class Meta:
        widgets = {
            'producer': ModelSelect2(url='producer-autocomplete'),
            'duty': ModelSelect2(url='duty-autocomplete'),
            'movie': ModelSelect2(url='movie-autocomplete')
        }
        model = ProducerMovieDuty
        fields = ('__all__')


class CompanyMovieDutyForm(forms.ModelForm):
    class Meta:
        widgets = {
            'company': ModelSelect2Multiple(url='company-autocomplete'),
            'duty': ModelSelect2(url='duty-autocomplete'),
            'movie': ModelSelect2(url='movie-autocomplete')
        }
        model = CompanyMovieDuty
        fields = ('__all__')

    #     #company = forms.ModelMultipleChoiceField()
    #     #duty = forms.ModelChoiceField(queryset=Duty.objects.all())
    #     #movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    #
    #     fields = ('__all__')
    #
    # def save(self, commit=True):
    #     for c in self.company:
    #         o = ProducerMovieDuty(Producer=c, Movie=self.movie, Duty=self.duty)
    #         o.save()

class BatchAddForm(forms.Form):
    company = forms.MultipleChoiceField(widget=Select2Multiple(url='company-autocomplete'))
    duty = forms.ChoiceField(widget=Select2('duty-autocomplete'))
    movie = forms.ChoiceField(widget=Select2(url='movie-autocomplete'))


    class Meta:
        # widgets = {
        #     'company': Select2(url='company-autocomplete'),
        #     'duty': Select2(url='duty-autocomplete'),
        #     'movie': Select2(url='movie-autocomplete')
        # }


    # class Meta:
        fields = ['company','duty','movie']


class BatchAddPMDForm(forms.Form):
    producer = forms.MultipleChoiceField(widget=Select2Multiple(url='producer-autocomplete'))
    duty = forms.ChoiceField(widget=Select2('duty-autocomplete'))
    movie = forms.ChoiceField(widget=Select2(url='movie-autocomplete'))


    class Meta:
        # widgets = {
        #     'company': Select2(url='company-autocomplete'),
        #     'duty': Select2(url='duty-autocomplete'),
        #     'movie': Select2(url='movie-autocomplete')
        # }


    # class Meta:
        fields = ['producer','duty','movie']

