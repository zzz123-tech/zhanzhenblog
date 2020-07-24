from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post
from .forms import CommentForm
from django.views.decorators.http import require_POST
from django.contrib import messages

@require_POST
def comment(request,post_pk):
    post = get_object_or_404(Post,pk=post_pk)
    form = CommentForm(request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()
        messages.add_message(request,messages.SUCCESS,'评论发表成功',extra_tags='success')
        return redirect(post)
    context = {
            'form':form,
            'post':post,
            }
    messages.add_message(request, messages.ERROR, '评论发表失败！请修改表单中的错误后重新提交。', extra_tags='danger')
    return render(request,'comments/preview.html',context=context)








# Create your views here.
