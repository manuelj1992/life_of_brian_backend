from django.contrib import admin
from .models import Contributors, WorksSingle, Single, Source, SourceSingle
# Register your models here.


admin.site.register(Contributors)
admin.site.register(WorksSingle)
admin.site.register(Single)
admin.site.register(SourceSingle)
admin.site.register(Source)
