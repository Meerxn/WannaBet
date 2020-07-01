from django.contrib import admin
from WannaBet.models import Profile, Bet, Event, Relationship, Sides
# Register your models here.

class RelationshipInline(admin.StackedInline):
    model = Relationship
    fk_name = 'from_profile'

class ProfileAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

# class SidesInline(admin.StackedInline):
#     model = Bet
#     name= "side_choices"

# class BetAdmin(admin.ModelAdmin):
#     inlines = [SidesInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Bet)
admin.site.register(Sides)
admin.site.register(Event)

