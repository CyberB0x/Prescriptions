import weasyprint
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Prescription
from .forms import PrescriptionForm
from django.template.loader import render_to_string


def create_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescriptions_list')  # или detail
    else:
        form = PrescriptionForm()
    return render(request, 'prescriptions/create.html', {'form': form})

def prescription_detail(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    context = {'prescription': prescription}
    return render(request, 'prescriptions/prescription_detail.html', context)

def download_prescription_pdf(request, pk):
    prescription = get_object_or_404(Prescription, pk=pk)
    html = render_to_string('prescriptions/pdf.html', {'prescription': prescription})
    pdf = weasyprint.HTML(string=html).write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename="prescription_{prescription.pk}.pdf"'
    return response

def prescription_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'prescriptions/prescription_list.html', {'prescriptions': prescriptions})