from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.indexpage, name='index'),
    path('home', views.indexpage, name='index'),
    path('home/', views.indexpage, name='index'),
    path('about/', views.aboutpage, name='about' ),
    path('contact/', views.contacnpage, name='contact' ),
    path('contact', views.contacnpage, name='contact' ),
    path('blog/', views.blogpage, name='blog' ),
    path('blog', views.blogpage, name='blog' ),
    path('services/', views.servicespage, name='services' ),
    path('services', views.servicespage, name='services' ),
    path('work/', views.workpage, name='work' ),
    path('work', views.workpage, name='work' ),
    path('flask', views.flaskpage, name='flask' ),
    path('flask/', views.flaskpage, name='flask' ),
    path('login/', views.sign_in, name='login'),
    path('logout/', views.sign_out, name='logout'),
    
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)