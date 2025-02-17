import time
from django.shortcuts import render
from .models import Project, Resume

def home_view(request):
    # Загружаем данные резюме
    resume = Resume.objects.first()

    # Загружаем список проектов
    projects = list(Project.objects.values("id", "title", "short_desc", "url", "image"))

    # Передаём данные в шаблон
    context = {
        "user_name": resume.full_name if resume else "Имя не задано",
        "email": resume.email if resume else "email@example.com",
        "telegram": "komihal7",  # Можно брать из Resume
        "projects": projects,
        "resume": resume,  # Передаём объект резюме
    }
    return render(request, "home.html", context)

def about_view(request):
    return render(request, 'about.html')

def projects_view(request):
    start_time = time.time()
    all_projects = Project.objects.all().order_by('-created_at')
    mid_time = time.time()
    print("[DEBUG] Query took:", mid_time - start_time)

    response = render(request, 'projects.html', {'projects': all_projects})
    end_time = time.time()
    print("[DEBUG] Render took:", end_time - mid_time)

    return response

def projects_by_category_view(request, category):
    # Фильтруем проекты по нужной категории
    filtered_projects = Project.objects.filter(category=category).order_by('-created_at')
    return render(request, 'projects_by_category.html', {
        'projects': filtered_projects,
        'category': category
    })

def resume_view(request):
    # Либо просто рендерить статическую страницу с резюме
    # Либо можно сделать модель Resume и хранить данные в БД — зависит от твоего подхода
    return render(request, 'resume.html')

def resume(request):
    resume = Resume.objects.first()  # Получаем первое резюме
    return render(request, "resume.html", {"resume": resume})