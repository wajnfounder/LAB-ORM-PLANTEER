from django.shortcuts import render
from .models import Plant
from .forms import PlantForm
from django.shortcuts import redirect, get_object_or_404
from .models import Plant, Comment

# Create your views here.



def all_plants_view(request):

    plants = Plant.objects.all()

    category = request.GET.get('category')
    edible = request.GET.get('edible')

    if category:
        plants = plants.filter(category=category)

    if edible == 'true':
        plants = plants.filter(is_edible=True)

    return render(request, 'plants/all.html', {
        'plants': plants,
        'categories': Plant.Category.choices,
        'selected_category': category,   
        'selected_edible': edible      
    })



def plant_detail_view(request, id):
    plant = get_object_or_404(Plant, id=id)
    comments = plant.comments.all().order_by('-created_at')

    if request.method == 'POST':
        Comment.objects.create(
            plant=plant,
            name=request.POST.get('name'),
            content=request.POST.get('content'),
        )
        return redirect(f'/plants/{id}/detail/')

    return render(request, 'plants/detail.html', {
        'plant': plant,
        'comments': comments,
    })





def create_plant_view(request):

    if request.method == 'POST':
        name = request.POST.get('name')
        about = request.POST.get('about')
        used_for = request.POST.get('used_for')
        image = request.FILES.get('image')
        category = request.POST.get('category')
        is_edible = request.POST.get('is_edible') == 'on'

        Plant.objects.create(
            name=name,
            about=about,
            used_for=used_for,
            image=image,
            category=category,
            is_edible=is_edible
        )

        return redirect('/plants/all/')

    return render(request, 'plants/new.html')






def update_plant_view(request, id):
    plant = get_object_or_404(Plant, id=id)

    if request.method == 'POST':
        plant.name = request.POST.get('name')
        plant.about = request.POST.get('about')
        plant.used_for = request.POST.get('used_for')

       
        image = request.FILES.get('image')
        if image:
            plant.image = image

       
        category = request.POST.get('category')
        print("CATEGORY:", category)  

        if not category:
            category = plant.category  

        plant.category = category

        plant.is_edible = request.POST.get('is_edible') == 'on'

        plant.save()
        return redirect('/plants/all/')

    return render(request, 'plants/update.html', {'plant': plant})






def delete_plant_view(request, id):
    plant = get_object_or_404(Plant, id=id)
    plant.delete()
    return redirect('/plants/all/')





def search_view(request):
    query = request.GET.get('q')

    plants = Plant.objects.all()

    if query:
        plants = plants.filter(name__icontains=query)

    return render(request, 'plants/all.html', {
        'plants': plants,
        'categories': Plant.Category.choices,
        'selected_category': None,
        'selected_edible': None
    })





def add_plant(request):
    if request.method == 'POST':
        form = PlantForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('all_plants')
    else:
        form = PlantForm()

    return render(request, 'plants/new.html', {'form': form})



