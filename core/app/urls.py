from django.urls import path, include
from rest_framework.routers import DefaultRouter

from core.app.views import (
    UserViewSet,
    RegisterView,
    TokenRefreshView,
    LoginView,
    TeamMemberViewSet,
    SlideViewSet,
    ServiceViewSet,
    ProjectViewSet,
    NewsViewSet,
    CompanyViewSet,
    AboutViewSet,
    ApplicationViewSet,
    GalleryViewSet,
)

router = DefaultRouter()
router.register("users", UserViewSet, "users")
router.register("team-members", TeamMemberViewSet, "team-members")
router.register("slides", SlideViewSet, "slides")
router.register("services", ServiceViewSet, "services")
router.register("projects", ProjectViewSet, "projects")
router.register("news", NewsViewSet, "news")
router.register("companies", CompanyViewSet, "companies")
router.register("about", AboutViewSet, "about")
router.register("applications", ApplicationViewSet, "applications")
router.register("gallery", GalleryViewSet, "gallery")

urlpatterns = [
    path("", include(router.urls)),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/refresh/", TokenRefreshView.as_view(), name="refresh"),
    path("auth/login/", LoginView.as_view(), name="login"),
]
