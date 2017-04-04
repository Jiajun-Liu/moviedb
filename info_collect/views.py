from django.shortcuts import render, render_to_response, HttpResponseRedirect
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
        movie = Movie.objects.get(pk=request.POST['movie'])
        request.session['movie'] = (movie.id, str(movie))
        # print(request.POST)
        added = []
        # print(request.POST.get('company'))
        clist = request.POST.getlist('company')
        for c in clist:
            # print('getting', c)
            o = CompanyMovieDuty(company=ProdCompany.objects.get(pk=c), movie=movie, duty=Duty.objects.get(
                pk=request.POST['duty']))
            # try:
            # print('adding',o)
            o.save()
            added.append(o)
            # except Exception as e:
            #    print(e)

        return render(request, 'batch_add_cmd.html', {'added': added, 'movie': request.session.get('movie')})
    else:
        return render(request, 'batch_add_cmd.html', {'movie': request.session.get('movie')})


@login_required
def batch_add_cmd11m(request):

    if request.method == 'POST':
        movie = Movie.objects.get(pk=request.POST['movie'])
        request.session['movie'] = (movie.id, str(movie))
        # print(request.POST)
        added = []
        # print(request.POST.get('company'))
        dlist = request.POST.getlist('duty')
        for c in dlist:
            # print('getting', c)
            o = CompanyMovieDuty(company=ProdCompany.objects.get(pk=request.POST['company']), movie=movie,
                                 duty=Duty.objects.get(pk=c))
            # try:
            # print('adding',o)
            o.save()
            added.append(o)
            # except Exception as e:
            #    print(e)

        return render(request, 'batch_add_cmd11m.html', {'added': added, 'movie': request.session.get('movie')})
    else:
        return render(request, 'batch_add_cmd11m.html', {'movie': request.session.get('movie')})


@login_required
def batch_add_pmd(request):
    if request.method == 'POST':
        added = []
        dl = request.POST.getlist('duty')
        pl = request.POST.getlist('producer')
        company = ProdCompany.objects.get(pk=request.POST.get('company')) if request.POST.get('company') else None
        movie = Movie.objects.get(pk=request.POST['movie'])
        request.session['movie'] = (movie.id, str(movie))

        if dl and len(dl) > 0 and len(dl) == len(pl):  # multiple duty/producer pairs

            for idx in range(len(dl)):
                o = ProducerMovieDuty(producer=Producer.objects.get(pk=pl[idx]), movie=movie, duty=Duty.objects.get(
                    pk=dl[idx]), company=company)
                o.save()
                added.append(o)
        else:
            added = ['The number of producers and duties must match']

        return render(request, 'batch_add_pmd.html', {'added': added, 'movie': request.session.get('movie')})
    else:
        return render(request, 'batch_add_pmd.html', {'movie': request.session.get('movie')})
