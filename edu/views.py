from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    edu = Edu.objects.all()
    context = {
		'edu': edu,
		'title': 'Список новостей',
		'subtitle': 'Самые свежые новости'
	}
    return render(request, 'edu/index.html', context)