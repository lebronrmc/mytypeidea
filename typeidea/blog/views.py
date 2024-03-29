#from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Tag,Post,Category
#from config.models import SideBar
# Create your views here.

from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from config.models import SideBar
from .models import Post, Category, Tag


class CommonViewMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sidebars': SideBar.get_all(),
        })
        context.update(Category.get_navs())
        return context


class IndexView(CommonViewMixin, ListView):
    queryset = Post.latest_posts()
    paginate_by = 5
    context_object_name = 'post_list'
    template_name = 'blog/list.html'


class CategoryView(IndexView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = self.kwargs.get('category_id')
        category = get_object_or_404(Category, pk=category_id)
        context.update({'category': category, })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        category_id = self.kwargs.get('category_id')
        return queryset.filter(category_id=category_id)


class TagView(IndexView):
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        tag_id = self.kwargs.get('tag_id')
        tag = get_object_or_404(Tag, pk=tag_id)
        context.update({'tag': tag, })
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        tag_id = self.kwargs.get('tag_id')
        return queryset.filter(tag_id=tag_id)


class PostDetailView(CommonViewMixin, DetailView):
    queryset = Post.latest_posts()
    template_name = 'blog/detail.html'
    context_object_name = 'post'
    pk_url_kwarg = 'post_id'


def post_list(request,category_id=None,tag_id=None):
    #content = 'post_list category_id={category_id},tag_id={tag_id}'.format(
    #    category_id=category_id,
    #    tag_id=tag_id,
    #)
    #return HttpResponse(content)
    tag = None
    category = None

    #if tag_id:
    #   try:
    #       tag = Tag.objects.get(id=tag_id)
    #   except Tag.DoesNotExist:
    #       post_list = []
    #   else:
    #       post_list = tag.post_set.filter(status=Post.STATUS_NORMAL)
    #lse:
    #   post_list = Post.objects.filter(status=Post.STATUS_NORMAL)
    #   if category_id:
    #       try:
    #           category = Category.objects.get(id=category_id)
    #       except Category.DoesNotExist:
    #           category = None
    #       else:
    #           post_list = post_list.filter(category_id=category_id)

    if tag_id:
        post_list,tag = Post.get_by_tag(tag_id)
    elif category_id:
        post_list,category = Post.get_by_category(category_id)
    else:
        post_list = Post.latest_posts()

    context = {
        'category':category,
        'tag':tag,
        'post_list':post_list,
        'sidebard':SideBar.get_all(),
    }
    context.update(Category.get_navs())
    return render(request,'blog/list.html ',context=context)

def post_detail(request,post_id=None):
    #return HttpResponse('detail')
    try:
        post = Post.objects.get(id=post_id)
    except Post.DoesNotExist:
        post = None
    context = {'post': post,
               'sidebard': SideBar.get_all(),
    }

    context.update(Category.get_navs())
    return render(request,'blog/detail.html',context=context)





