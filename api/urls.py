from django.urls import path, include
from rest_framework.routers import SimpleRouter
from api.views import (
    IndexView, CategoriesView, ContactIconsView, EducationView, ExperienceView, PersonalInfoView, SkillView,
    WorkView,
)

router = SimpleRouter()
router.register('categories', CategoriesView, basename='category')
router.register('contactIcons', ContactIconsView, basename='contact icon')
router.register('education', EducationView, basename='education')
router.register('experience', ExperienceView, basename='experience')
router.register('personal_info', PersonalInfoView)
router.register('skill', SkillView)
router.register('work', WorkView, 'work')

urlpatterns = [
    path('', IndexView.as_view()),
    path('', include(router.urls)),
]