from .models import Categories

def getCategories(request):
    categoriesName = Categories.objects.all()
    return {'categoriesName':categoriesName}