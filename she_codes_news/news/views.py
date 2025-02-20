from django.views import generic
from django.urls import reverse_lazy, reverse 
from .models import NewsStory, Comment, Category
from .forms import StoryForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.contrib.auth.decorators import login_required


class IndexView(generic.ListView):
    template_name = 'news/index.html'

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.order_by('-pub_date')[:4]
        # context['old_stories'] = NewsStory.objects.all().order_by('pub_date') [:5]
        context['all_stories'] = NewsStory.objects.order_by('-pub_date')

        # liked_story = get_object_or_404(NewsStory, id=self.kwargs['pk'])
        # total_likes = liked_story.total_likes()
        # context['total_likes'] = total_likes

        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'
    # is_favourite = False

    # def story_detail(request, id):
    #     if story.likes.filter(id=request.user.id).exists():

class AddStoryView(generic.CreateView):
    model = NewsStory
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

# def favourite_post(request, id):
#     story = get_object_or_404(NewsStory, id=id)
#     if story.favourite.filter(id = request.user.id).exists():
#         story.favourite.remove(request.user)
#     else: 
#         story.favourite.add(request.user)
#     return redirect('news:story', pk=story.id)

@login_required
def favourite_post(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    user = request.user
    if story.favourite.filter(id=user.id).exists():
        story.favourite.remove(user)
    else:
        story.favourite.add(user)
    return redirect('news:story', pk=story.id)

def favourite_post_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts
    }
    return render(request, 'news/favourite_post_list.html', context)

@login_required
def like_post(request, pk):
    story = get_object_or_404(NewsStory, pk=pk)
    user = request.user
    if story.liked_by.filter(id=user.id).exists():
        story.liked_by.remove(user)
    else:
        story.liked_by.add(user)
    return redirect('news:story', pk=story.id)


def CategoryView(request, cats):
    category_posts = NewsStory.objects.filter(category=cats)
    return render(request, 'news/categories.html', {'cats':cats, 'category_posts':category_posts})

class AddCategoryView(generic.CreateView):
    model = Category
    # form_class = StoryForm
    # context_object_name = 'storyForm'
    template_name = 'news/add_category.html'
    fields = "__all__"
    success_url = reverse_lazy('news:index')

    # success_url = reverse_lazy('news:index')

class AddCommentView(generic.CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'news/add_comment.html'
    success_url = reverse_lazy('news:index')
    # def get_success_url(self):
    #     return reverse_lazy('news:story', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

class EditStoryView(generic.UpdateView):
    form_class = StoryForm
    model = NewsStory
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

class DeleteStoryView(generic.DeleteView):
    model = NewsStory
    template_name = 'news/deleteStory.html'
    success_url = reverse_lazy('news:index')

