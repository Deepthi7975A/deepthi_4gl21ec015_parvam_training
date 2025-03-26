from django.shortcuts import render, redirect, get_object_or_404
from .models import College
from .forms import CollegeForm
from django.contrib import messages

# List all colleges
def college_list(request):
    colleges = College.objects.all()
    return render(request, 'college_crud/list_book.html', {'colleges': colleges})

# Create a new college
def college_create(request):
    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'College added successfully!')
            return redirect('college_list')
    else:
        form = CollegeForm()
    return render(request, 'college_crud/college_create.html', {'form': form})

# Update college details
def college_update(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid():
            form.save()
            messages.success(request, 'College updated successfully!')
            return redirect('college_list')
    else:
        form = CollegeForm(instance=college)
    return render(request, 'college_crud/collefe_create.html', {'form': form})

# View college details
def college_detail(request, pk):
    college = get_object_or_404(College, pk=pk)
    return render(request, 'college_crud/college_detail.html', {'college': college})

# Update college details
def college_update(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid():
            form.save()
            messages.success(request, 'College updated successfully!')
            return redirect('college_list')
        else:
            messages.error(request, 'Error updating college. Please check the form.')
    else:
        form = CollegeForm(instance=college)
    
    return render(request, 'college_crud/college_create.html', {'form': form, 'update': True, 'college': college})

# Delete college record
def college_delete(request, pk):
    college = get_object_or_404(College, pk=pk)
    if request.method == 'POST':
        college.delete()
        messages.success(request, 'College deleted successfully!')
        return redirect('college_list')
    return render(request, 'college_crud/college_delete.html', {'college': college})