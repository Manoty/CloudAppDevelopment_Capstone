from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    
   path('', views.index, name='index'),
   path('about/', views.about, name='about'),
   path('contact/', views.contact, name='contact'),
    # path for about view

    # path for contact us view

    # path for registration

    # path for login

    # path for logout

    path(route='', view=views.get_dealerships, name='index'),

    # path for dealer reviews view

    # path for add a review view

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)