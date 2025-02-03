from django.contrib import admin
from django.urls import path, include
from home import views


urlpatterns = [
    path('', views.home, name='home'),
    path('gallary', views.gallary, name='gallary'),
    path('<pk>/preview', views.preview, name='preview'),
    path('about', views.about, name='about'),
    path('packages', views.packages, name='packages'),
    path('<pk>/packages', views.shoPackages, name='show-packages'),
    path('contact', views.addContact, name='contact'),
    path('messages', views.showMessages, name='show-messages'),
    path('<pk>/replies/',views.seeReplies, name='see-replies'),
    path('contact-soon', views.contactSoon, name='contact-soon'),
    path('<pk>/reply/',views.replyPost , name='reply-comment'),
]
