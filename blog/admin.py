from django.contrib import admin
from .models import Post  # 여기가 추가된줄
# Register your models here.

#admin.site.register(Post) #admin에다가 Post모델을 등록한다 # 여기가 추가된줄
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_at']
    list_filter = ['updated_at']
    search_fields = ['title']


