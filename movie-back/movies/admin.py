from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(User)
admin.site.register(Genre)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(Review)
admin.site.register(Worldcup)
admin.site.register(Ranking)