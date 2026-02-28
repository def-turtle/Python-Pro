from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from django.conf import settings

LOG_FILE = settings.BASE_DIR / 'login_times.log'

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    ts = timezone.now().isoformat()
    ip = request.META.get('REMOTE_ADDR', '')
    line = f"{ts} - {user.username} - {ip}\n"
    try:
        with open(LOG_FILE, 'a', encoding='utf-8') as f:
            f.write(line)
    except Exception:
        pass