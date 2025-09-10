from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Animal, Toy, Habitat
from .forms import AnimalForm, ToyForm, HabitatForm, SignupForm

# Home
def home(request):
    return render(request, "my_app/home.html")

# -----------------------
# Animal CRUD
# -----------------------
@login_required
def animal_index(request):
    animals = Animal.objects.filter(owner=request.user)
    return render(request, "my_app/animal_index.html", {"animals": animals})

@login_required
def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk, owner=request.user)
    return render(request, "my_app/animal_detail.html", {"animal": animal})

@login_required
def animal_create(request):
    if request.method == "POST":
        form = AnimalForm(request.POST)
        if form.is_valid():
            animal = form.save(commit=False)
            animal.owner = request.user
            animal.save()
            return redirect("animal_index")
    else:
        form = AnimalForm()
    return render(request, "my_app/animal_form.html", {"form": form})

@login_required
def animal_update(request, pk):
    animal = get_object_or_404(Animal, pk=pk, owner=request.user)
    form = AnimalForm(request.POST or None, instance=animal)
    if form.is_valid():
        form.save()
        return redirect("animal_detail", pk=animal.pk)
    return render(request, "my_app/animal_form.html", {"form": form})

@login_required
def animal_delete(request, pk):
    animal = get_object_or_404(Animal, pk=pk, owner=request.user)
    if request.method == "POST":
        animal.delete()
        return redirect("animal_index")
    return render(request, "my_app/animal_confirm_delete.html", {"animal": animal})

# -----------------------
# Toy CRUD
# -----------------------
@login_required
def toy_index(request):
    toys = Toy.objects.filter(animal__owner=request.user)
    return render(request, "my_app/toy_index.html", {"toys": toys})

@login_required
def toy_detail(request, pk):
    toy = get_object_or_404(Toy, pk=pk, animal__owner=request.user)
    return render(request, "my_app/toy_detail.html", {"toy": toy})

@login_required
def toy_create(request):
    if request.method == "POST":
        form = ToyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("toy_index")
    else:
        form = ToyForm()
    return render(request, "my_app/toy_form.html", {"form": form})

@login_required
def toy_update(request, pk):
    toy = get_object_or_404(Toy, pk=pk, animal__owner=request.user)
    form = ToyForm(request.POST or None, instance=toy)
    if form.is_valid():
        form.save()
        return redirect("toy_detail", pk=toy.pk)
    return render(request, "my_app/toy_form.html", {"form": form})

@login_required
def toy_delete(request, pk):
    toy = get_object_or_404(Toy, pk=pk, animal__owner=request.user)
    if request.method == "POST":
        toy.delete()
        return redirect("toy_index")
    return render(request, "my_app/toy_confirm_delete.html", {"toy": toy})

# -----------------------
# Habitat CRUD (Many-to-Many)
# -----------------------
@login_required
def habitat_index(request):
    habitats = Habitat.objects.all()
    return render(request, "my_app/habitat_index.html", {"habitats": habitats})

@login_required
def habitat_detail(request, pk):
    habitat = get_object_or_404(Habitat, pk=pk)
    return render(request, "my_app/habitat_detail.html", {"habitat": habitat})

@login_required
def habitat_create(request):
    if request.method == "POST":
        form = HabitatForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("habitat_index")
    else:
        form = HabitatForm()
    return render(request, "my_app/habitat_form.html", {"form": form})

@login_required
def habitat_update(request, pk):
    habitat = get_object_or_404(Habitat, pk=pk)
    form = HabitatForm(request.POST or None, instance=habitat)
    if form.is_valid():
        form.save()
        return redirect("habitat_detail", pk=habitat.pk)
    return render(request, "my_app/habitat_form.html", {"form": form})

@login_required
def habitat_delete(request, pk):
    habitat = get_object_or_404(Habitat, pk=pk)
    if request.method == "POST":
        habitat.delete()
        return redirect("habitat_index")
    return render(request, "my_app/habitat_confirm_delete.html", {"habitat": habitat})

# -----------------------
# Signup
# -----------------------
def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = SignupForm()
    return render(request, "registration/signup.html", {"form": form})