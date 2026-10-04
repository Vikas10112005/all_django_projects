from django.http import HttpResponse


def test_sos(request):
    return HttpResponse('<h1>this is my first project</h1>')
