from django_http import HttpResponse


def index(request):
    return HttpResponse("<h1> Crudapp")
