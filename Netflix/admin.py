from django.contrib import admin
from .models import Series
from .models import Movies
from .models import Anime
from .models import Sitcom
from .models import Cartoon


# Register your models here.
admin.site.register(Series)
admin.site.register(Movies)
admin.site.register(Anime)
admin.site.register(Sitcom)
admin.site.register(Cartoon)

