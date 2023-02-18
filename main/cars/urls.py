from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.cars, name='cars'),
    path("info_car/<int:id>/", views.info_car, name="Car"),
    path("order_car/", views.order_car, name='order_car'),
    path("rent/", views.rent, name='rent'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


