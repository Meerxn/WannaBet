from django.db import models
import uuid
from django.contrib.auth.models import User
import random
import string
# Create your models here.

# A profile can have many bets
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)
    profile_score = models.IntegerField(blank=True)
    
    # bets = models.ForeignKey(Bet, on_delete=models.CASCADE)
    def score(self):
        self.profile_score = (self.wins / self.wins + self.losses) * 100
        super(Profile, self).save()


class Event(models.Model):
    name = models.CharField(max_length = 30)
    # type = 
    # time = 
    # outcome = 
    link = models.URLField(blank=True)

class Bet(models.Model):
    event = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
   
    name = models.CharField(max_length = 30)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    url = models.URLField(blank = True)
    # members = 
    # challange = 
    # event = 


    # Can generate 2 billion unique IDs
    def id_gen(size=6, chars=string.ascii_letters+ string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self):
        if not self.id:
            self.id = f"#{id_gen()}"
            while MyModel.objects.filter(id=self.id).exists():
                self.id = f"#{id_gen()}"
        super(Bet, self).save()


class Challange(models.Model):
    bet = models.ForeignKey(Bet, on_delete = models.CASCADE)
    choices_for_challanges = [
        ('M', 'Money'),
        ('A', 'Activity'),
        ('G', 'Gift')
    ]
    
    name = models.CharField(max_length = 30)
    type = models.CharField(max_length = 1, choices = choices_for_challanges)
    descrition = models.TextField()


