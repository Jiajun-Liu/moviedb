from django.contrib import admin
from .models import *
from .forms import *
from django.shortcuts import render, render_to_response, HttpResponseRedirect
from django.template import RequestContext
from .models import *
from dal_select2.views import Select2QuerySetView
from .forms import BatchAddForm
from django.conf.urls import url


class MovieAdmin(admin.ModelAdmin):
    fields = ('title', 'year', 'boxoffice', 'code')
    list_display = ('title', 'year', 'boxoffice')
    search_fields = ('title', 'year')

    autocomplete_lookup_fields = {
        'title': ['title'],
    }


class ProducerAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


class DutyAdmin(admin.ModelAdmin):
    fields = ('name',)
    list_display = ('name',)
    search_fields = ('name',)


class ProdCompanyAdmin(admin.ModelAdmin):
    fields = ('name', 'location', 'capital', 'scope', 'industry')
    list_display = ('name', 'location', 'capital')
    search_fields = ('name', 'location', 'capital', 'scope', 'industry')


class ProducerMovieDutyAdmin(admin.ModelAdmin):
    fields = ('producer', 'movie', 'duty', 'company')
    list_display = ('producer_name', 'movie_name', 'duty_name', 'company_name')
    search_fields = ('producer__name', 'movie__title', 'duty__name', 'company__name')

    def producer_name(self, obj):
        return u'%s' % obj.producer.name

    producer_name.short_description = u'Producer'

    def movie_name(self, obj):
        return u'%s' % obj.movie.title

    movie_name.short_description = u'Movie'

    def duty_name(self, obj):
        return u'%s' % obj.duty.name

    duty_name.short_description = u'Duty'

    def company_name(self, obj):
        if obj.company:
            return u'%s' % obj.company.name
        else:
            return 'None'

    company_name.short_description = u'Company'

    form = ProducerMovieDutyForm


class CompanyMovieDutyAdmin(admin.ModelAdmin):
    fields = ('company', 'movie', 'duty')
    list_display = ('company_name', 'movie_name', 'duty_name')
    search_fields = ('company__name', 'movie__name', 'duty__name')

    def company_name(self, obj):
        return u'%s' % obj.company.name

    company_name.short_description = u'Company'

    def movie_name(self, obj):
        return u'%s' % obj.movie.title

    movie_name.short_description = u'Movie'

    def duty_name(self, obj):
        return u'%s' % obj.duty.name

    duty_name.short_description = u'Duty'
    form = CompanyMovieDutyForm


# class BtachAddCMDAdmin(admin.ModelAdmin):
#     def get_urls(self):
#         urls = super().get_urls()
#         my_urls = [
#             url(r'^batch_add/$', self.my_view),
#         ]
#         return my_urls + urls
#
#     def my_view(self, request):
#         if request.method == 'POST':
#             # form = BatchAddForm(request.POST)
#             print(request.POST)
#             added = []
#             print(request.POST.get('company'))
#             for c in request.POST.getlist('company'):
#                 print('getting', c)
#                 o = CompanyMovieDuty(company=ProdCompany.objects.get(pk=c), movie=Movie.objects.get(pk=request.POST[
#                     'movie']), duty=Duty.objects.get(pk=request.POST['duty']))
#                 # try:
#                 print('adding', o)
#                 o.save()
#                 added.append(o)
#                 # except Exception as e:
#                 #    print(e)
#             # if form.is_valid():
#             # form.save()
#             form = BatchAddForm()
#             return render(request, 'batch_add.html', {'form': form, 'added': added})
#         else:
#             form = BatchAddForm()
#             return render(request, 'batch_add.html', {'form': form})

admin.site.register(Movie, MovieAdmin)
admin.site.register(ProdCompany, ProdCompanyAdmin)
admin.site.register(Producer, ProducerAdmin)
admin.site.register(Duty, DutyAdmin)
admin.site.register(ProducerMovieDuty, ProducerMovieDutyAdmin)
admin.site.register(CompanyMovieDuty, CompanyMovieDutyAdmin)
# admin.site.register(BtachAddCMDAdmin)


admin.site.site_header = 'Movie Production Industry Database Administration'
admin.site.site_title = 'Movie Production Industry Database Administration'
admin.site.index_title = 'Administration'
# admin.site.add_action()
