from django.shortcuts import render
from django.urls import reverse
from django.utils.translation import activate

# Create your views here.

def index(request):
    return render(request, "internatiolization/index.html", {})



def language_switcher(request):
    lang = request.LANGUAGE_CODE
    if lang == 'en':
        url = reverse('set_language', kwargs={'lang_code': 'es'})
        lang_name = 'Español'
    else:
        url = reverse('set_language', kwargs={'lang_code': 'en'})
        lang_name = 'English'
    return f'<a href="{url}" onclick="event.preventDefault();document.getElementById(\'language-form\').submit();">{lang_name}</a>' \
           f'<form id="language-form" method="post" action="{url}">' \
           f'{request.csrf_token}' \
           f'<input type="hidden" name="next" value="{request.path}">' \
           f'</form>'