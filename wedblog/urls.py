from django.urls import path
import wedblog.views

urlpatterns = [
    path('new/', wedblog.views.new, name='new'),
    path('create/', wedblog.views.create, name='create'),
    #path('newblog/', wedblog.views.blogpost,name='nowblog')
]

