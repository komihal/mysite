from django.contrib import admin
from pages.models import Project
from .models import Resume, Experience, Skill

# Register your models here.
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')
    # или любой другой набор опций

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

class SkillInline(admin.TabularInline):
    model = Skill
    extra = 3

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("full_name", "job_title", "city", "phone", "email")
    inlines = [ExperienceInline, SkillInline]

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ("company", "position", "start_date", "end_date")

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name",)