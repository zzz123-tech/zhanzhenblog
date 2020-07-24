from django.db import models
from django.utils import timezone

class Comment(models.Model):
    name = models.CharField('名字',max_length=30)
    email = models.EmailField()
    url = models.URLField('网址',blank=True)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    post = models.ForeignKey('blog.Post',verbose_name='文章',on_delete=models.CASCADE)
    class Meta():
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']
    def __str__(self):
        return '{}: {}'.format(self.name,self.text[:20])



# Create your models here.
