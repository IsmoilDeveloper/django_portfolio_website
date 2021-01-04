from django.shortcuts import render

# Create your views here.
def works(request):
    context = {'works': 'active'}
    return render(request, 'work/works.html', context)
