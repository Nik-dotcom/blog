from django.shortcuts import redirect, render
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm, AddNewPost

# Create your views here.

class PostView(View):
    '''
    Вывод записей
    '''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})


class PostDetail(View):
    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        return render(request, "blog/blog_detail.html", {'post': post})


class AddPost(View):
    def get(self,request):
        form  = AddNewPost()
        return render(request, "blog/add_post.html", {'form': form})
    
    def post(self,request):
        form  = AddNewPost(request.POST, request.FILES)
        if form.is_valid():
            form = form.save(commit=False)
            form.author = request.user
            form.save()
            return redirect('/')
        return render(request, "blog/add_post.html", {'form': form})

class AddComments(View):
    def post(self, request, pk):
        if request.method == 'POST':
            if pk:
                form  = CommentsForm(request.POST)
                if form.is_valid():
                    form = form.save(commit=False)
                    form.post_id = pk
                    form.user = request.user
                    form.save()
                
        return redirect(f'/{pk}/')