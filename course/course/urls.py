"""course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from login.views import login1, sign, main, course, contact, c, cpp, java, python, django, network,logout1,CHECK,signup1
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login1, name="login"),
    path('CHECK/', CHECK, name="CHECK"),
    path('signup1/', sign, name="signup1"),
    path('signup/', signup1, name="signup"),
    path('mainpage/', main, name="mainpage"),
    path('course/', course, name="course"),
    path('contact/', contact, name="contact"),
    path('c/', c, name="c"),
    path('cpp/', cpp, name="cpp"),
    path('java/', java, name="java"),
    path('python/', python, name="python"),
    path('django/', django, name="django"),
    path('network/', network, name="network"),
    path('logout/',logout1,name="logout"),
]
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)