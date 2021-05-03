import os
from datetime import datetime

# Fix for Python 2.x.
try:
    input = raw_input
except NameError:
    pass

import django
from django.conf import settings
from django.core.management.utils import get_random_secret_key

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

settings.configure(
    DEBUG=True,
    TEMPLATES=[dict(
        BACKEND='django.template.backends.django.DjangoTemplates',
        APP_DIRS=True,
        DIRS=[
            os.path.join(BASE_DIR, 'config'),
        ],
    )],
)

try:
    django.setup()
except AttributeError:
    pass

from django.template.loader import get_template

settings_template = get_template("settings.template.py")

def ask_text(need, default=None):
    need = need.strip()
    if default:
        msg = "%s Default: [%s] : " % (need, default)
    else:
        msg = "%s : " % need

    while True:
        response = input(msg)
        if response:
            return response
        elif default is not None:
            return default
        else:
            pass

if __name__ == "__main__":

    context = {
        'now': str(datetime.now()),
        'secret_key': get_random_secret_key(),
    }

    secret = ask_text("Google Secret")
    client_id = ask_text("Google Client ID")
    context['google'] = dict(secret=secret, client_id=client_id)

    with open('config/settings.py', 'w') as out:
        out.write(settings_template.render(context, request=None))
    print("Settings rendered successfully")
