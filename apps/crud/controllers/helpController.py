from django.shortcuts import render, redirect, get_object_or_404

from apps.crud.forms.helpForm import HelpForm
from apps.crud.models.help import Help


def help_list(request, template_name='apps/crud/help/help_list.html'):
    helps = Help.objects.all()
    data = {}
    data['object_list'] = helps
    return render(request, template_name, data)


def help_create(request, template_name='apps/crud/help/help_form.html'):
    form = HelpForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('help_list')
    return render(request, template_name, {'form': form})


def help_update(request, pk, template_name='apps/crud/help/help_form.html'):
    help = get_object_or_404(Help, pk=pk)
    form = HelpForm(request.POST or None, instance=help)
    if form.is_valid():
        form.save()
        return redirect('help_list')
    return render(request, template_name, {'form': form})


def help_delete(request, pk, template_name='apps/crud/help/help_confirm_delete.html'):
    help = get_object_or_404(Help, pk=pk)
    if request.method == 'POST':
        help.delete()
        return redirect('help_list')
    return render(request, template_name, {'object': help})
