from django.shortcuts import render


# Create your views here.
def index(request):
    # data = {
    #     'title': 'Главная страница',
    #     'values': ['test_str', 69, 86.2, True],
    #     'person_obj': {
    #         'name': 'Вася',
    #         'age': 23,
    #         'hobby': 'coding'
    #     }}
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def contact(request):
    return render(request, 'main/contact.html')
