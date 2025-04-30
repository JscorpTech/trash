from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

################################
# Admin Panel
################################
urlpatterns = [
    path("backend/admin/", admin.site.urls),
    path("backend/i18n/", include("django.conf.urls.i18n")),
]

################################
# App Routes
################################
urlpatterns += [
    path("backend/api/", include("core.app.urls")),
]

################################
# API Schema & Docs
################################
urlpatterns += [
    path("backend/api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "backend/api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("backend/api/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]

################################
# Static Files
################################
urlpatterns += static("backend/" + settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static("backend/" + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
