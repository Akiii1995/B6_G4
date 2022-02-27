from django.apps import AppConfig

print("in apps.py")
class BookAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Book_App'
