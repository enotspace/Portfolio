#from django.utils.translation import gettext_lazy as _
from django.template import loader
from django.http import HttpResponse

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())