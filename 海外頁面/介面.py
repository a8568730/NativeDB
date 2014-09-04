from django.shortcuts import render

from django.http import HttpResponse
from django.template import RequestContext, loader
from django.views import generic
from django.shortcuts import get_object_or_404
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.db.models import Q
from django.views.generic.base import View

def 首頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/first.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 主頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/index.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))

def 細節描述頁(request):
# 	output = ', '.join([p.title for p in latest_poll_list])
# 	return HttpResponse(output)
	template = loader.get_template('海外頁面/details.html')
	context = RequestContext(request, {
	})
	return HttpResponse(template.render(context))
