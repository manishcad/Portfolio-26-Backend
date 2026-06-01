from django.urls import path
from .views import (
    ContactCreateView, SkillListView, ProjectListView, ExperienceListView,
    EducationListView, LanguageListView
)

urlpatterns = [
    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('skills/', SkillListView.as_view(), name='skill-list'),
    path('projects/', ProjectListView.as_view(), name='project-list'),
    path('experience/', ExperienceListView.as_view(), name='experience-list'),
    path('education/', EducationListView.as_view(), name='education-list'),
    path('languages/', LanguageListView.as_view(), name='language-list'),
]
