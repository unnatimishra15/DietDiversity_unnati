from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from search import views as search_views

urlpatterns = [
    url(r'^django-admin/', admin.site.urls),
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^search/$', search_views.search, name='search'),
    url('', include("HomePage.urls")),
    url(r'student/',include("Login.urls")),
    url(r'recipeform/',include("RecipeForm.urls")),
    url(r'foodform/',include("FoodForm.urls")),
    url(r'coordinator/',include("Coordinator.urls")),
    url(r'student/',include("RegistrationForm.urls")),
    url(r'mentor/',include("Mentor.urls")),
    url(r'submission/',include("StudentSubmission.urls")),
    url(r'school/',include("Schoolregistration.urls")),
    url(r'dayspending/',include("Day.urls")),
    url(r'display/',include(("Display.urls",'Display'),namespace='Display')),
    url(r'dietrecall/',include("DietRecallApp.urls")),
    url(r'teacher/',include("TeacherRegistration.urls")),
    url(r'camera/',include("CameraApp.urls")),
    url(r'mapimage/',include("MapImage.urls")),
    url(r'bulkregistration/',include("UsersRegistration.urls")),
    
]



if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    from django.conf.global_settings import DATETIME_INPUT_FORMATS

# ISO 8601 datetime format to accept html5 datetime input values
    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    DATETIME_INPUT_FORMATS += ["%Y-%m-%dT%H:%M:%S", "%Y-%m-%dT%H:%M"]
urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    url(r"", include(wagtail_urls)),

    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    url(r"^pages/", include(wagtail_urls)),
]
