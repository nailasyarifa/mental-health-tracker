from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306245882',
        'name': 'Naila Syarifa Yosarvi',
        'class': 'PBP E'
    }

    return render(request, "main.html", context)
