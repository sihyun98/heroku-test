from django.shortcuts import render, get_object_or_404, redirect
from .models import Wedblog
from django.utils import timezone
from django.core.paginator import Paginator

def home(request):
    wedblogs = Wedblog.objects
    wedblog_list = Wedblog.objects.all()
    paginator = Paginator(wedblog_list,3)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'home.html',{'wedblogs':wedblogs, 'posts':posts})

def new(request):
    return render(request, 'new.html')

def create(request):
    wedblog = Wedblog()
    wedblog.title = request.GET['title']
    wedblog.body = request.GET['body']
    wedblog.pub_date = timezone.datetime.now()
    wedblog.save()
    return redirect('/')

def detail(request, wedblog_id):
    wedblog_detail = get_object_or_404(Wedblog, pk=wedblog_id)
    return render(request, 'detail.html', {'wedblog': wedblog_detail})
