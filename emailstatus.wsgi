import os
import sys

path = '/var/wsgi'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'emailstatus.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
