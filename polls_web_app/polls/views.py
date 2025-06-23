from django.http import HttpResponse


def index(request):
    return HttpResponse("Bonjour les dia 3")