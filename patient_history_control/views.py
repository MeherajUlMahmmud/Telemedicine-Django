from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required

from user_control.models import *
from .forms import *


@login_required(login_url="login")
def history_home_view(request, pk):
    patient = PatientModel.objects.get(id=pk)
    history = HistoryModel.objects.filter(user=patient)

    # paginator = Paginator(history, 10)
    # page = request.GET.get("page", 1)
    #
    # try:
    #     history = paginator.page(page)
    # except PageNotAnInteger:
    #     history = paginator.page(1)
    # except EmptyPage:
    #     history = paginator.page(paginator.num_pages)

    context = {
        "history": history,
    }
    return render(request, "pages/patient-history/history-control-home.html", context)


@login_required(login_url="login")
def history_create_view(request):
    task = "Create New"
    form = AddEditHistoryForm()
    if request.method == "POST":
        form = AddEditHistoryForm(request.POST, request.FILES)
        if form.is_valid():
            history = form.save(commit=False)
            history.user = request.user
            history.save()
            return redirect("patient-history-detail", id=history.id)
    context = {
        "task": task,
        "form": form,
    }
    return render(request, "pages/patient-history/history-create-update.html", context)


@login_required(login_url="login")
def history_detail_view(request, pk):
    history = HistoryModel.objects.get(id=pk)
    patient = history.user
    edit_access = False
    if request.user.is_authenticated and request.user.is_patient:
        if request.user == patient.user:
            edit_access = True

    context = {
        "history": history,
        "edit_access": edit_access,
    }
    return render(request, "pages/patient-history/history-detail.html", context)


@login_required(login_url="login")
def history_update_view(request, pk):
    task = "Update"
    history = HistoryModel.objects.get(id=pk)
    form = AddEditHistoryForm(instance=history)

    if request.method == "POST":
        form = AddEditHistoryForm(request.POST, request.FILES, instance=history)
        if form.is_valid():
            form.save()
            return redirect("patient-history-detail", id=history.id)

    context = {
        "task": task,
        "form": form,
        "history": history,
    }

    return render(request, "pages/patient-history/edit-history.html", context)


@login_required(login_url="login")
def history_delete_view(request, pk):
    history = HistoryModel.objects.get(id=pk)

    if request.method == 'POST':
        history.delete()
        return redirect("patient-history-home")

    context = {
        "history": history,
    }

    return render(request, "pages/patient-history/delete-history.html", context)
