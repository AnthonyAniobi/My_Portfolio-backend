from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import (
    CategoriesView, ContactIconsView, EducationView, ExperienceView,
    WorkView,
)

router = SimpleRouter()
# router.register('', IndexView, basename='index')
router.register('categories', CategoriesView, basename='category')
router.register('contactIcons', ContactIconsView, basename='contact icon')
router.register('education', EducationView, basename='education')
router.register('experience', ExperienceView, basename='experience')
router.register('work', WorkView, 'work')

urlpatterns = router.urls