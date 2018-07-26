from django.contrib import admin

from .models import Album
from .models import Song

@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
      pass

@admin.register(Song)
class AlbumAdmin(Song.ModelAdmin):
      pass
