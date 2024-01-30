from rest_framework.routers import DefaultRouter
from products.api.api_views.product_views import ProductViewSet

router = DefaultRouter()

router.register(r'products', ProductViewSet, basename='products')

urlpatterns = router.urls