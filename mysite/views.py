from django.shortcuts import render


def show_map(request):
    return render(request, 'start_page.html')