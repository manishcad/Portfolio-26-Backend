from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"


class Skill(models.Model):
    name = models.CharField(max_length=100)
    # e.g., 'Frontend', 'Backend', 'Database', 'AI'
    category = models.CharField(max_length=100)
    # Proficiency level from 1 to 100
    level = models.PositiveIntegerField(default=80)

    def __str__(self):
        return self.name


class Technology(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    project_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    technologies = models.ManyToManyField(Technology, related_name="projects")
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.titlel


class Experience(models.Model):
    role = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.role} at {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.degree} from {self.institution}"


class Language(models.Model):
    name = models.CharField(max_length=100)
    # e.g., 'Native', 'Fluent', 'Professional', 'Conversational'
    proficiency = models.CharField(max_length=100)
    # Proficiency level from 1 to 100 for the progress bar
    level = models.PositiveIntegerField(default=90)

    def __str__(self):
        return self.name
