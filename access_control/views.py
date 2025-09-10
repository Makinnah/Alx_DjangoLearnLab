from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Resource
from .forms import ResourceForm

@permission_required('access_control.can_view', raise_exception=True)
def resource_list(request):
    resources = Resource.objects.all()
    return render(request, 'access_control/resource_list.html', {'resources': resources})

@permission_required('access_control.can_create', raise_exception=True)
def resource_create(request):
    form = ResourceForm(request.POST or None)
    if form.is_valid():
        resource = form.save(commit=False)
        resource.created_by = request.user
        resource.save()
        return redirect('resource_list')
    return render(request, 'access_control/resource_form.html', {'form': form})

@permission_required('access_control.can_edit', raise_exception=True)
def resource_edit(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    form = ResourceForm(request.POST or None, instance=resource)
    if form.is_valid():
        form.save()
        return redirect('resource_list')
    return render(request, 'access_control/resource_form.html', {'form': form})

@permission_required('access_control.can_delete', raise_exception=True)
def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    resource.delete()
    return redirect('resource_list')
