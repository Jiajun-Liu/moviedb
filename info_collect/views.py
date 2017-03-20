from django.shortcuts import render, render_to_response,HttpResponseRedirect
from django.template import RequestContext
from .models import *
from dal_select2.views import Select2QuerySetView
from .forms import BatchAddForm, BatchAddPMDForm

def index(request):
    return render(request, 'index.html')


class MovieAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Movie.objects.none()

        qs = Movie.objects.all()
        if self.q:
            qs = qs.filter(title__icontains=self.q)

        return qs


class ProducerAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Producer.objects.none()

        qs = Producer.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class DutyAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Duty.objects.none()
        #
        qs = Duty.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs


class CompanyAutocomplete(Select2QuerySetView):
    def get_queryset(self):
        # Don't forget to filter out results depending on the visitor !
        # if not self.request.user.is_authenticated():
        #     return Duty.objects.none()
        #
        qs = ProdCompany.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)

        return qs

# def batch_add_cmd(request):
#     if request.method == 'POST':
#         #form = BatchAddForm(request.POST)
#         #print(request.POST)
#         added = []
#         #print(request.POST.get('company'))
#         for c in request.POST.getlist('company'):
#             #print('getting', c)
#             o = CompanyMovieDuty(company=ProdCompany.objects.get(pk=c), movie=Movie.objects.get(pk=request.POST[
#                 'movie']), duty=Duty.objects.get(pk=request.POST['duty']))
#             #try:
#             #print('adding',o)
#             o.save()
#             added.append(o)
#             #except Exception as e:
#             #    print(e)
#         #if form.is_valid():
#         #form.save()
#         form = BatchAddForm()
#         return render(request, 'batch_add.html', {'form': form, 'added': added})
#     else:
#         form = BatchAddForm()
#         return render(request, 'batch_add.html', {'form': form})
#
from django.contrib.auth.decorators import login_required

@login_required
def batch_add_cmd(request):
    if request.method == 'POST':
        #print(request.POST)
        added = []
        #print(request.POST.get('company'))
        for c in request.POST.getlist('company'):
            #print('getting', c)
            o = CompanyMovieDuty(company=ProdCompany.objects.get(pk=c), movie=Movie.objects.get(pk=request.POST[
                'movie']), duty=Duty.objects.get(pk=request.POST['duty']))
            #try:
            #print('adding',o)
            o.save()
            added.append(o)
            #except Exception as e:
            #    print(e)

        return render(request, 'batch_add_cmd.html', {'added': added})
    else:
        return render(request, 'batch_add_cmd.html', {})

@login_required
def batch_add_pmd(request):
    if request.method == 'POST':
        #form = BatchAddForm(request.POST)
        #print(request.POST)
        added = []
        #print(request.POST.get('producer'))
        for c in request.POST.getlist('producer'):
            #print('getting', c)
            o = ProducerMovieDuty(producer=Producer.objects.get(pk=c), movie=Movie.objects.get(pk=request.POST[
                'movie']), duty=Duty.objects.get(pk=request.POST['duty']),company=ProdCompany.objects.get(pk=request.POST[
                'company']))
            #try:
            #print('adding',o)
            o.save()
            added.append(o)
            #except Exception as e:
            #    print(e)
        #if form.is_valid():
        #form.save()
        form = BatchAddPMDForm()
        return render(request, 'batch_add_pmd.html', {'form': form, 'added': added})
    else:
        form = BatchAddPMDForm()
        return render(request, 'batch_add_pmd.html', {'form': form})