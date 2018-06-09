import json

from django.core.exceptions import ValidationError
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic.base import View
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse

from recruitment.models import UserProfile


# Create your views here.

class Recruiter(View):
    template_name = 'recruitment_form.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(Recruiter, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return TemplateResponse(request, self.template_name, {})

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        data = request.POST
        try:
            UserProfile.objects.create(name=data['full_name'],
                                     email=data['email'],
                                     gender=data['gender'],
                                     dob=data['dob'],
                                     phone_number=data['phone_number'],
                                     address=data['address'],
                                     total_experience=data['total_experience'])
            return HttpResponse(json.dumps({'response': 'Form submit successfully'}), content_type='application/json', status=200)
        except (ValueError, ValidationError):
            return  HttpResponse(json.dumps({'response': 'Incorrect field value'}), content_type='application/json', status=400)

class RecruiterList(View):
    template_name = 'recruiter_list.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(RecruiterList, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        if request.user.is_superuser:
            context = [{'id': i.id, 'name': i.name,
                        'email': i.email,
                        'gender': i.gender,
                        'dob': i.dob,
                        'phone_number': i.phone_number,
                        'address': i.address,
                        'total_experience': i.total_experience,
                    } for i in UserProfile.objects.filter(status='pending')]
            return TemplateResponse(request, self.template_name, {'data': context})
        return TemplateResponse(request, 'bad_request.html', {}) 

    def post(self, request, *args, **kwargs):
        data = request.POST
        user_profile = UserProfile.objects.get(id=data['id'])
        user_profile.status = data['status']
        user_profile.save()
        return HttpResponse(json.dumps({'response': 'Form updated successfully'}), content_type='application/json', status=200)

class AdminLogin(View):
    template_name = 'recruiter_list.html'

    def get(self, request):
        return TemplateResponse(request, 'login.html', {}) 
