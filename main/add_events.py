from scorespro import find_data
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
import django
django.setup()

from WannaBet.models import Event

[[0,1,2,3],[0,1,2,3]]
#    main_sports.append([leauge_name, home, score, away, match_kick_str])

def add_soccer_events(matches):
    for match in matches:
        event = Event.objects.get_or_create(name = f"{match[0]}: {match[1]} vs {match[3]}")
    
if __name__ == "__main__":
    url = 'https://www.scorespro.com/'
    add_soccer_events(find_data(url))