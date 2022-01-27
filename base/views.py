from django.shortcuts import render

rooms = [
    {
        'id': 1,
        'name': "Room 1",
    },
    {
        'id': 2,
        'name': "Room 2",
    },
    {
        'id': 3,
        'name': "Room 3",
    },
]

def home(request):
    return render(request, 'base/home.html', {'rooms': rooms})

def room(request, pk):
    room = None
    for i in rooms:
        if(i['id'] == int(pk)):
            room = i
            break
    context = {'room': room}
    return render(request, 'base/room.html', context)

