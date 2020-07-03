from django.db import models
import uuid
from django.contrib.auth.models import User
import random
import string
from django.utils import timezone
# Create your models here.

# A profile can have many bets
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    # For Following People 
    relationships = models.ManyToManyField('self', through='Relationship', symmetrical=False, related_name='related_to')

    wins = models.IntegerField(default = 0)
    losses = models.IntegerField(default = 0)

    
    # bets = models.ForeignKey(Bet, on_delete=models.CASCADE)

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)


class Relationship(models.Model):
    from_profile = models.ForeignKey(Profile, related_name='from_people', on_delete=models.CASCADE)
    to_profile = models.ForeignKey(Profile, related_name='to_people', on_delete=models.CASCADE)
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)

    def get_relationships(self, status):
        return self.relationships.filter(
            to_people__status=status,
            to_people__from_profile=self)

    def get_related_to(self, status):
        return self.related_to.filter(
            from_people__status=status,
            from_people__to_profile=self)

    def get_following(self):
        return self.get_relationships(RELATIONSHIP_FOLLOWING)

    def get_followers(self):
        return self.get_related_to(RELATIONSHIP_FOLLOWING)


# Add Event Details later
class Event(models.Model):
    name = models.CharField(max_length = 30)
    time = models.DateTimeField(default=timezone.now)
    link = models.URLField(blank=True)

    # categories = ['Sports', 'Gaming', 'Board games']
    # types_of_events = ['Football', 'Basketball/']

    # category = models.CharField(max_length = 280, choices = categories, default="Uncategorized")
    # type_of_event = models.CharField(max_length = 280, choices = types_of_events, default="Uncategorized")

class Bet(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="for_event", null = True)
    # members = models.ManyToManyField(User, related_name="bet_member")
    name = models.CharField(max_length = 30)
    descrition = models.TextField(blank=True)
    identifier = models.CharField(max_length = 7, blank = True)
    side = models.ManyToManyField(User, through='Sides', related_name="side_to")
    
    url = models.URLField(blank = True)
    
    choices_for_challanges = [
        ('M', 'Money'),
        ('A', 'Activity'),
        ('G', 'Gift')
    ]
    
    choices_for_sides = [
        ('W', 'Win'),
        ('L', 'Loss'),
        ('D', 'Draw')
    ]

    
    def get_members(self):
        return self.members

    type = models.CharField(max_length = 1, choices = choices_for_challanges, default="None")
    
    # Can generate 2 billion unique IDs
    def idgen(size=6, chars=string.ascii_letters+ string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self, *args, **kwargs):
        super(Bet, self).save(*args, **kwargs)
        if not self.identifier:
            self.identifier = f"{(''.join(random.choice(string.ascii_letters+ string.digits) for _ in range(6)))}"
            while Bet.objects.filter(identifier=self.identifier).exists():
                self.identifier = f"{(''.join(random.choice(string.ascii_letters+ string.digits) for _ in range(6)))}"
        super(Bet, self).save(*args, **kwargs)

class Sides(models.Model):
    profile = models.ForeignKey(User, on_delete = models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete= models.CASCADE, related_name="side_choices")
    choices_for_sides = [
        ('W', 'Win'),
        ('L', 'Loss'),
        ('D', 'Draw')
    ]
    
    side = models.CharField(max_length = 1, choices = choices_for_sides)


