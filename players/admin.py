from django.contrib import admin

# Register your models here.
from players.models import players_list
admin.site.register(players_list)
