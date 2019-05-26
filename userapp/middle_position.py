from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
import re

class ForceLogin(MiddlewareMixin):
    def process_response(self, request, response):

        path = request.path
        if re.findall('^/main/',path) or re.findall('^/cart/',path) :
            request.session['path'] = request.path
        return response  # 必须返回response