from django.shortcuts import render


def test_view(request):
    return render(request, "base.html", {})

# Create your views here.
