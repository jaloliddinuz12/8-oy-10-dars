from rest_framework.routers import SimpleRouter, DefaultRouter

from .views import PuplesViewSet, ClassViewSet

router = DefaultRouter()

router.register('puples', PuplesViewSet, basename='uquvchi')
router.register('class', ClassViewSet)

urlpatterns = router.urls