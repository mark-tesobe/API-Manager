# -*- coding: utf-8 -*-
"""
Views for base app
"""

from django.conf import settings
from django.views.generic import TemplateView
from django.shortcuts import render
from obp.forms import DirectLoginForm, GatewayLoginForm
from obp.api import API, APIError

def get_banks(request):
    api = API(request.session.get('obp'))
    try:
        urlpath = '/banks'
        result = api.get(urlpath)
        if 'banks' in result:
            return [bank['id'] for bank in sorted(result['banks'], key=lambda d: d['id'])]
        else:
            return []
    except APIError as err:
        messages.error(self.request, err)
        return []

class HomeView(TemplateView):
    """View for home page"""
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'API_HOST': settings.API_HOST,
            'logo_url': settings.LOGO_URL,
            'override_css_url': settings.OVERRIDE_CSS_URL,
            'directlogin_form': DirectLoginForm(),
            'ALLOW_DIRECT_LOGIN':settings.ALLOW_DIRECT_LOGIN,
            'gatewaylogin_form': GatewayLoginForm(),
            'ALLOW_GATEWAY_LOGIN': settings.ALLOW_GATEWAY_LOGIN,
            'SHOW_API_TESTER':settings.SHOW_API_TESTER,
            'API_TESTER_URL':settings.API_TESTER_URL
        })
        return context



