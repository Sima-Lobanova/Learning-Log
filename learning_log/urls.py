from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Админка Django
    path('admin/', admin.site.urls),

    # Включение URL-адресов из приложения learning_logs
    path('', include('learning_logs.urls')),
]
