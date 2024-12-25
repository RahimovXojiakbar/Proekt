from rest_framework.routers import SimpleRouter
from . import views


router = SimpleRouter()

router.register('president', views.PresidentViewSet, basename='president')
router.register('state', views.StateViewSet, basename='state')
router.register('governor-region', views.GovernorRegionViewSet, basename='governor-region')
router.register('region', views.RegionViewSet, basename='region')
router.register('governor-district', views.GovernorDistrictViewSet, basename='governer-district')
router.register('district', views.DistrictViewSet, basename='district')
router.register('chairman', views.ChairmanViewSet, basename='chairman')
router.register('MFY', views.MFYViewSet, basename='MFY')
router.register('neighborhood', views.NeighborhoodViewSet, basename='neighborhood')
router.register('house', views.HouseViewSet, basename='house')
router.register('human', views.HumanViewSet, basename='human')


urlpatterns = router.urls