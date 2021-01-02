from django.shortcuts import *
from django.views.generic import *
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
# rendering the home page
class PostListView(ListView):
    model = Post
    paginate_by = 6
    #ordering = ['-timestamp']  template_name = 'blog/index.html'
    template_name = 'blog/index.html'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-timestamp')[:3]
        return context


# details page for each product
class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-timestamp')[:3]
        comment_form = CommentForm()
        context['comment_form'] = comment_form
        return context

#rendering create view
class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog/post_new.html'
    fields = '__all__'

#rendering update view
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'overview', 'content', 'image', 'categories', 'featured']


#rendering delete view
class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')


#rendering signup view
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/signup.html'


# rendering contact page
def contact(request):
    context = {}
    return render(request, 'blog/contact.html', context)

# rendering about page
def about(request):
    context = {}
    return render(request, 'blog/about.html', context)

