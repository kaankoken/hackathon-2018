"""
Definition of urls for DjangoWebProject2.
"""


from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
import app.forms
import app.views
    
# Uncomment the next lines to enable the admin:
# from django.conf.urls import include
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about', app.views.about, name='about'),
    url(r'^registration', app.views.registration, name='registration'),
    url(r'^înst_registration', app.views.inst_registration, name='inst_registration'),
    url(r'^client_main', app.views.client_main, name='client_main'),
    url(r'^institution_main', app.views.institution_main, name='institution_main'),
    url(r'^my_reservation', app.views.my_reservation, name='my_reservation'),
    url(r'^my_modules', app.views.my_modules, name='my_modules'),
    url(r'^my_labs', app.views.my_labs, name='my_labs'),
    url(r'^user_registration', app.views.user_registration, name='user_registration'),
    url(r'^admin', admin.site.urls),
    url(r'^institution', app.views.log_inst, name='institution'),
    url(r'^client', app.views.log_user, name='client'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^login_Inst/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login_Ins.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Institution',
                'year': datetime.now().year,
            }
        },
        name='Institution'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
