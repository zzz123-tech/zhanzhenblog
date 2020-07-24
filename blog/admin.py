from django.contrib import admin
from .models import Post,Tag,Category
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','created_time','modified_time','category','author']
    fields = ['title','body','excerpt','category','tags']
    def save_model(self,request,obj,form,change):
        obj.author = request.user
        super().save_model(request,obj,form,change)
admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Category)
# Register your models here.
