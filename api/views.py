from django.shortcuts import render
from rest_framework import generics
from .models import Contact, Skill, Project, Experience, Education, Language
from .serializers import (
    ContactSerializer, SkillSerializer, ProjectSerializer, ExperienceSerializer,
    EducationSerializer, LanguageSerializer
)

# Create your views here.
class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class SkillListView(generics.ListAPIView):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer


class ProjectListView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ExperienceListView(generics.ListAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class EducationListView(generics.ListAPIView):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer


class LanguageListView(generics.ListAPIView):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
