from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.shortcuts import render
from .models import Url


@login_required
def urls_list(request):
    urls = Url.objects.all()
    data = serialize('json', urls)
    return render(request, 'urls/urls.html',
                  context={'urls': urls, 'data': data})
