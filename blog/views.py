# /blog/views.py
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Post, Comment
from .forms import PostForm, CommentForm


# 글 목록 불러오는 함수
def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    posts = Post.objects.all() #모든 글을 불러오려면 이렇게 쓸 수 있나봐
    q = request.GET.get('q', '')    # 검색 기능
    if q:
        qs = qs.filter(title__icontains=q)
    return render(request, 'blog/post_list.html', {
        'posts': posts,
    })  #'post_list': posts,


# # 글 초안 (draft) 목록 불러오는 함수
# @login_required
# def post_draft_list(request):
#     posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
#     return render(request, 'blog/post_draft_list.html', {
#         'posts': posts
#     })


# 글의 세부 내용 불러오는 함수
def post_detail(request, pk):   # 여기서 pk는 id 같은 것
    # try:
    #     post = Post.objects.get(id=id)
    # except Post.DoesNotExist:
    #     raise Http404             # 아래와 같은 표현이다 (감싸주는 것임)
    post = get_object_or_404(Post, pk=pk)   # 404 에러 나오도록 한다
    return render(request, 'blog/post_detail.html', {'post': post})


# 글쓰기 함수
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)    # 뒤에 request.FILES 추가함
        if form.is_valid():     # 유효성 검사 수행
            post = form.save(commit=False)
            # messages.add_message(request, messages.INFO, '새 글이 등록되었습니다.')
            messages.success(request, '새 글이 등록되었습니다.')
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
            form = PostForm()
    return render(request, 'blog/post_form.html', {'form': form})


# 글 수정 함수
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            messages.success(request, '글이 수정되었습니다.')
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'form': form})


# 글 publish 함수
@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)


# 글 지우기 함수
@login_required
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')


# 댓글 쓰는 함수
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})


# 댓글 승인 함수 (승인을 받아야 댓글이 달린다)
@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


# 댓글 제거 함수
@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_list(request):
    comment_list = Comment.objects.all().select_ralated('post')
    return render(request, 'blog/comment_list.html', {
        'comment_list' : comment_list,
    })
