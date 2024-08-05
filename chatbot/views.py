from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def chat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = 'This would be an AI response.'
        return JsonResponse({'message': message, 'response': response})
    return render (request, 'chat.html')
