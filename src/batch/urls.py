from django.urls import path, include
from . import views
from rest_framework import routers
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

router = routers.DefaultRouter()
router.register('batch/import', views.BatchView)
router.register('batch/import-integrity', views.BatchIntegrityView)
router.register('batch/import-tstx', views.TimestampTransactionView)

urlpatterns = [
    path('', include(router.urls)),
    path('batch/import/new/', views.BatchView.as_view({'get': 'require_integrity'}))
]

urlpatterns += staticfiles_urlpatterns()