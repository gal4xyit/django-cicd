from django.shortcuts import render


def home(request):
    return render(request, "pages/page.html", {
        "title": "Головна",
        "description": "Вітаємо! Це Django-сайт із трьома сторінками для практичної роботи з CI/CD.",
    })


def about(request):
    return render(request, "pages/page.html", {
        "title": "Про проєкт",
        "description": "Мета проєкту — налаштувати автоматичне тестування, збірку Docker-образу та його публікацію в Docker Hub через GitHub Actions.",
    })


def contacts(request):
    return render(request, "pages/page.html", {
        "title": "Контакти",
        "description": "Це сторінка контактної інформації навчального проєкту з DevOps.",
    })
