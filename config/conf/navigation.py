from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


def user_has_group_or_permission(user, permission):
    if user.is_superuser:
        return True

    group_names = user.groups.values_list("name", flat=True)
    if not group_names:
        return True

    return user.groups.filter(permissions__codename=permission).exists()


PAGES = [
    {
        "seperator": True,
        "items": [
            {
                "title": _("Home"),  # Home page
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Users"),  # Users
        "items": [
            {
                "title": _("Users"),
                "icon": "person_add",
                "link": reverse_lazy("admin:app_usermodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_user"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Application"),  # Application
        "items": [
            {
                "title": _("Applications"),  # Applications
                "icon": "assignment",
                "link": reverse_lazy("admin:app_applicationmodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_application"
                ),
            },
        ],
    },
    {
        "seperator": True,
        "title": _("Content"),  # Content
        "items": [
            {
                "title": _("About"),  # About
                "icon": "info",
                "link": reverse_lazy("admin:app_aboutmodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_about"
                ),
            },
            {
                "title": _("News"),  # News
                "icon": "article",
                "link": reverse_lazy("admin:app_newsmodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_news"
                ),
            },
            {
                "title": _("Slides"),  # Slides
                "icon": "slideshow",
                "link": reverse_lazy("admin:app_slidemodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_slide"
                ),
            },
            {
                "title": _("Services"),  # Services
                "icon": "build",
                "link": reverse_lazy("admin:app_servicemodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_service"
                ),
            },
            {
                "title": _("Projects"),  # Projects
                "icon": "work",
                "link": reverse_lazy("admin:app_projectmodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_project"
                ),
            },
            {
                "title": _("Gallery"),  # Projects
                "icon": "work",
                "link": reverse_lazy("admin:app_gallerymodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_project"
                ),
            },
            {
                "title": _("Company"),  # Company
                "icon": "business",
                "link": reverse_lazy("admin:app_companymodel_changelist"),
                "permission": lambda request: user_has_group_or_permission(
                    request.user, "view_company"
                ),
            },
        ],
    },
]
