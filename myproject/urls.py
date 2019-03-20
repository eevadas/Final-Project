from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from UserInfo import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Blogs.urls')),
    path('starred/',user_views.starred,name='starred'),
    path('mypost/',user_views.myPost,name='mypost'),
    path('removestar/<int:id>',user_views.removeStar,name='removeStar'),
    path('starred/<int:id>',user_views.addStar,name='addStar'),

    path('profile/',user_views.profile,name='profile'),
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='UserInfo/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='UserInfo/logout.html'),name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
