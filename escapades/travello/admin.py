from django.contrib import admin
from  .models import Destination
from .models import Detailed_desc
from .models import Post
# Register your models here.

admin.site.register(Destination)
admin.site.register(Detailed_desc)
admin.site.register(Post)