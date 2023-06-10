from django.shortcuts import render, redirect

from .models import ScheduledRepair
from .forms import RepairForm

# Create your views here.

def index(request):
    return render(request, "index.html")

def repairs(request):
    queryset = ScheduledRepair.objects.all()
    form = RepairForm()

    if request.method == 'POST':
        form = RepairForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            repair = form.save(commit=False)
            repair.user = request.user
            repair.photo = form.cleaned_data['photo']
            repair.save()
            return redirect('repairs')

    context = {"repairs": queryset, "form": form}
    return render(request, "repairs.html", context)