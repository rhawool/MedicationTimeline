from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from datetime import datetime
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from timeline_app.forms import UpdateEntryDataForm
from timeline_app.models import IntakeEntry


@login_required
def home_page(request):
    try:
        last_entry1 = IntakeEntry.objects.all().last()
        last_entry = datetime.strptime(str(last_entry1), "%Y-%m-%d %H:%M:%S")

        context = {
            'last_entry': last_entry,
            'last_entry1': last_entry1,
        }
        return render(request, "home_page.html", context)
    except Exception as e:
        print(e)
        return render(request, "home_page.html", {})


@login_required
def add_entry(request):
    try:
        # dt = datetime.now()
        # dt2 = dt.strftime("%Y-%m-%d %H:%M:%S")
        # medicine_selection = request.GET.get("medicine_selection")
        # print(medicine_selection)
        #
        # medi_obj = Medicine.objects.get(name=medicine_selection)
        # new_entry = IntakeEntry.objects.create(intake_time=dt2, medicine_name=medi_obj)
        # new_entry.save()

        dt = datetime.now()
        dt2 = dt.strftime("%Y-%m-%d %H:%M:%S")
        medicine_selection = request.POST.get("medicine_selection")
        new_entry = IntakeEntry.objects.create(intake_time=dt2, medicine_name=medicine_selection)
        new_entry.save()

        messages.success(request, 'Entry Added Successfully')
        return redirect("home_page")
    except Exception as e:
        messages.error(request, f'Error adding entry. Error code/message: {e}')
        return redirect("home_page")


@login_required
def history_list(request):
    entries = IntakeEntry.objects.all().order_by('-id')

    context = {
        'entries': entries,
    }

    return render(request, "history_list.html", context)


@login_required
def delete_entries(request):
    try:
        selected_entries = request.POST.getlist("selected_entries")

        for entry in selected_entries:
            IntakeEntry.objects.get(id=entry).delete()

        messages.success(request, 'Entries Deleted Successfully')
        return redirect("history_list")

    except Exception as e:
        messages.error(request, f'Error deleting entry. Error code/message: {e}')
        return redirect("history_list")


class UpdateEntryData(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = IntakeEntry
    form_class = UpdateEntryDataForm
    template_name = 'update_entry.html'
    login_url = 'login_user'
    success_url = reverse_lazy('history_list')
    success_message = "Entry updated successfully"

    def get_success_message(self, cleaned_data):
        return self.success_message


def delete_single_entry(request, entry_id):
    IntakeEntry.objects.get(id=entry_id).delete()
    messages.success(request, 'Entry Deleted Successfully')
    return redirect("history_list")

# def medicine_list(request):
#     medicines = Medicine.objects.all()
#     form = AddMedicineForm()
#     context = {
#         'medicines': medicines,
#         'form': form,
#     }
#     return render(request, "medicine_list.html", context)
#
#
# def delete_medicine(request):
#     try:
#         selected_medicines = request.POST.getlist("selected_medicines")
#
#         for med in selected_medicines:
#             Medicine.objects.get(id=med).delete()
#
#         messages.success(request, 'Medicine/s Deleted Successfully')
#         return redirect("medicine_list")
#
#     except Exception as e:
#         messages.error(request, f'Error deleting Medicine/s. Error code/message: {e}')
#         return redirect("medicine_list")
#
#
# def add_medicine(request):
#
#     form = AddMedicineForm(request.POST)
#
#     if form.is_valid():
#         try:
#             form.save()
#             messages.success(request, "Medicine added successfully.")
#             return redirect("medicine_list")
#         except Exception as e:
#             messages.error(request, f"Error Adding Medicine. Error code/message: {e}")
#             return redirect("medicine_list")
#     else:
#         messages.error(request, "Invalid entries found. Please check and try again.")
#         return redirect("medicine_list")

