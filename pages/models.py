from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('construction', 'Строительные'),
        ('it', 'IT-приложения'),
        ('product', 'Управление продуктами'),
    ]

    title = models.CharField(max_length=200)
    short_desc = models.TextField()
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES,
        default='it'
    )
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    url = models.URLField(blank=True)  # если нужно вести на внешнюю страницу

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    from django.db import models

class Resume(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    job_title = models.CharField("Должность", max_length=255)
    phone = models.CharField("Телефон", max_length=20)
    email = models.EmailField("Email")
    city = models.CharField("Город", max_length=100)
    summary = models.TextField("О себе")
    photo = models.ImageField("Фото", upload_to="resume_photos/", blank=True, null=True)

    def __str__(self):
        return self.full_name
    
class Experience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="experiences")
    company = models.CharField("Компания", max_length=255)
    position = models.CharField("Должность", max_length=255)
    start_date = models.CharField("Дата начала", max_length=20)
    end_date = models.CharField("Дата окончания", max_length=20, blank=True, null=True)
    description = models.TextField("Описание")

    def __str__(self):
        return f"{self.company} – {self.position}"

class Skill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name="skills")
    name = models.CharField("Навык", max_length=100)

    def __str__(self):
        return self.name