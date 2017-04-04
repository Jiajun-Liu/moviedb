
from django.conf.urls import url
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^batch_add_cmd/', views.batch_add_cmd),
    url(r'^batch_add_cmd11m/', views.batch_add_cmd11m),
    url(r'^batch_add_pmd/', views.batch_add_pmd),
    url(r'^admin/', admin.site.urls),

    url(r'^movie-autocomplete/$', views.MovieAutocomplete.as_view(), name='movie-autocomplete'),
    url(r'^duty-autocomplete/$', views.DutyAutocomplete.as_view(), name='duty-autocomplete'),
    url(r'^producer-autocomplete/$', views.ProducerAutocomplete.as_view(), name='producer-autocomplete'),
    url(r'^company-autocomplete/$', views.CompanyAutocomplete.as_view(), name='company-autocomplete'),
]
