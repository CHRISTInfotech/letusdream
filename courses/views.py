from django.shortcuts import render


# Create your views here.
def yclpCourse(request):
    return render(request, 'courses/yclpCourse.html')
