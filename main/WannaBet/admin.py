from django.contrib import admin
from WannaBet.models import Profile, Bet, Event, Relationship, Sides
# Register your models here.
from django.contrib.contenttypes.admin import GenericTabularInline

class RelationshipInline(admin.StackedInline):
    model = Relationship
    fk_name = 'from_profile'

class ProfileAdmin(admin.ModelAdmin):
    inlines = [RelationshipInline]

# class SidesInline(admin.StackedInline):
#     model = Sides

class SidesInline(admin.TabularInline):
    model = Bet.side.through
    extra = 3

class BetAdmin(admin.ModelAdmin):
   inlines = (
        SidesInline,
        )

admin.site.register(Profile, ProfileAdmin)

admin.site.register(Bet, BetAdmin)
admin.site.register(Sides)
admin.site.register(Event)

