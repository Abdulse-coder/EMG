import pytz

TIME_ZONE = 'UTC'
USE_TZ = True

# Manually set default time zone using pytz
import django.utils.timezone
django.utils.timezone.activate(pytz.timezone(TIME_ZONE))
