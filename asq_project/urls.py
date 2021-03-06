"""asq_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include, url
from django.views.generic import RedirectView
from asq_app.views import signup

from asq_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/q/')),
]

urlpatterns += [
    path('q/', include('asq_app.urls')),
    url(r'^u/$',views.user_dashboard,name='user_dashboard'),
    url(r'^auth/', include('social_django.urls', namespace='social')),  # <- Here
    path('u/<int:uid>',views.common_user_dashboard,name='common_user_dashboard'),
    url(r'^search/', include('haystack.urls')),
    url(r'^froala_editor/', include('froala_editor.urls')),
]


#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path(r'accounts/signup/', views.signup),
    path('accounts/', include('django.contrib.auth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
