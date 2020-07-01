from django.db import models
import uuid
from django.contrib.auth.models import User
import random
import string
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
    time = models.DateTimeField(blank=True)
    link = models.URLField(blank=True)

class Bet(models.Model):
    event = models.ForeignKey(Event,null=True, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    members = models.ManyToManyField(Profile, through='Sides', symmetrical=False)
    name = models.CharField(max_length = 30)
    descrition = models.TextField(blank=True)
    

    url = models.URLField(blank = True)
    
    choices_for_challanges = [
        ('M', 'Money'),
        ('A', 'Activity'),
        ('G', 'Gift')
    ]
    
    type = models.CharField(max_length = 1, choices = choices_for_challanges, default="None")
   


    # Can generate 2 billion unique IDs
    def id_gen(size=6, chars=string.ascii_letters+ string.digits):
        return ''.join(random.choice(chars) for _ in range(size))

    def save(self):
        if not self.id:
            self.id = f"#{id_gen()}"
            while MyModel.objects.filter(id=self.id).exists():
                self.id = f"#{id_gen()}"
        super(Bet, self).save()

class Sides(models.Model):
    profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    bet = models.ForeignKey(Bet, on_delete= models.CASCADE, related_name="side_choices")
    choices_for_sides = [
        ('W', 'Win'),
        ('L', 'Loss'),
        ('D', 'Draw')
    ]
    
    side = models.CharField(max_length = 1, choices = choices_for_sides)
