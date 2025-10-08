from rest_framework.routers import DefaultRouter
from app.car.views import CarViewsetsAPI, CarNotification

router = DefaultRouter()
router.register('car', CarViewsetsAPI, basename='car')
router.register("car-notification", CarNotification, basename='notification')

urlpatterns = [
    
]

urlpatterns += router.urls