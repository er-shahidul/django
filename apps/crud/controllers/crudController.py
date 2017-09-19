from django.shortcuts import render, redirect, get_object_or_404

from apps.crud.forms.crudForm import CrudForm
from apps.crud.models.crud import Crud


def crud_list(request, template_name='apps/crud/crud/crud_list.html'):
    cruds = Crud.objects.all()
    data = {}
    data['object_list'] = cruds
    return render(request, template_name, data)


def crud_create(request, template_name='apps/crud/crud/crud_form.html'):
    form = CrudForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('crud_list')
    return render(request, template_name, {'form': form})


def crud_update(request, pk, template_name='apps/crud/crud/crud_form.html'):
    crud = get_object_or_404(Crud, pk=pk)
    form = CrudForm(request.POST or None, instance=crud)
    if form.is_valid():
        form.save()
        return redirect('crud_list')
    return render(request, template_name, {'form': form})


def crud_delete(request, pk, template_name='apps/crud/crud/crud_confirm_delete.html'):
    crud = get_object_or_404(Crud, pk=pk)
    if request.method == 'POST':
        crud.delete()
        return redirect('crud_list')
    return render(request, template_name, {'object': crud})
