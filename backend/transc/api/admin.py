from django.contrib import admin
from .models import User, FriendRequest
from .models import Tournament, Game, Notification
from .models import Channel, Message

# Register your models here.
admin.site.register(User)
admin.site.register(FriendRequest)
admin.site.register(Tournament)
admin.site.register(Game)
admin.site.register(Notification)
admin.site.register(Channel)
admin.site.register(Message)
