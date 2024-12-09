"""
URL configuration for Game_Kiroku_Django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include, reverse_lazy
from django.views.generic import CreateView

from games import views as games_views
from users.forms import CustomUserCreationForm

urlpatterns = [
    path('', games_views.index, name='index'),
    path('auth/', include('django.contrib.auth.urls')),
    path(
        'auth/registration',
        CreateView.as_view(
            template_name='registration/registration_form.html',
            form_class=CustomUserCreationForm,
            success_url=reverse_lazy('users:current_user_redirect'),
        ),
        name='registration'),
    path('admin/', admin.site.urls),
    path('games/', include('games.urls', namespace='games')),
    path('users/', include('users.urls', namespace='users')),
    path('developers/', include('developers.urls', namespace='developers')),
    path('publishers/', include('publishers.urls', namespace='publishers')),

]

if settings.DEBUG:
    import debug_toolbar
    from django.conf.urls.static import static

    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
