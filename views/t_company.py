from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required


from ..models import Company, Member


def company_list(request):
    companies = Company.objects.all()

    params = {}
    params['companies'] = companies

    return render(request, 'blog/company_list.html', params)
