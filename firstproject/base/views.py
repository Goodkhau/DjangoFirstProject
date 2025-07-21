from django.shortcuts import render


rooms = [
    {'id': 1, 'name':'Lets learn django!'},
    {'id': 2, 'name':'Design with me'},
    {'id': 3, 'name':'Fullstack Developer'}
]


def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    return render(request, 'base/room.html')