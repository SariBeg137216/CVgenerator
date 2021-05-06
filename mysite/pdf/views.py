from django.shortcuts import render
from .models import Profile
from django.http import HttpResponse
import pdfkit
from django.template import loader
# Create your views here.


def accept(request):
    if request.method == 'POST':
        name = request.POST.get('name', "")
        email = request.POST.get('email', "")
        phone = request.POST.get('phone', "")
        objective = request.POST.get('objective', "")
        skills = request.POST.get('skills', "")
        university = request.POST.get('university', "")
        degree = request.POST.get('degree', "")
        previous_work = request.POST.get('previous_work', "")

        profile = Profile(name=name, email=email, phone=phone, objective=objective, skills=skills, university=university, degree=degree, previous_work=previous_work)
        profile.save()

    return render(request, 'pdf/accept.html')


def user_profile(request, id):
    user = Profile.objects.get(id=id)
    template = loader.get_template('pdf/resume.html')
    html = template.render({'user': user})
    options = {
        "page-size": "letter",
        "encoding": "UTF-8",
    }
    pdf = pdfkit.from_string(html, False, options)
    response = HttpResponse(pdf, content_type='application/pdf')
    response["Content-Disposition"] = 'attachment'
    filename = "resume"
    return response


def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'pdf/profiles.html', {'profiles': profiles})

