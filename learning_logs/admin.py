from django.contrib import admin

# Register your models here.
from .models import Topic, Entry, Pizza, Topping

admin.site.register(Topic)
admin.site.register(Entry)
admin.site.register(Pizza)
admin.site.register(Topping)
