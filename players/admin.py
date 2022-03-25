from django.contrib import admin

# Register your models here.
from players.models import *
admin.site.register(players_list)
admin.site.register(Profile)
admin.site.register(Challenges)
admin.site.register(Notify)
admin.site.register(score)