from importlib.resources import path


from django.urls import path
from . import views # noktayı aynı dizinde olduğumuz için koyduk.

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about")
]