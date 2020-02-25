from django.shortcuts import render, redirect

from .models import StudentData


def home(request):
    students = StudentData.objects.all()
    context = {'students': students}
    return render(request, 'students/home.html', context)


def add_student(request):
    return render(request, 'students/add_student.html')


def save_data(request):
    sname = request.POST.get('sname')
    school = request.POST.get('school')
    cls = request.POST.get('cls')
    section = request.POST.get('section')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    telugu = request.POST.get('telugu')
    hindi = request.POST.get('hindi')
    english = request.POST.get('english')
    maths = request.POST.get('maths')
    science = request.POST.get('science')
    social = request.POST.get('social')
    data = StudentData(
        student_name=sname,
        school_name=school,
        class_name=cls,
        section=section,
        email=email,
        mobile=mobile,
        telugu_marks=telugu,
        hindi_marks=hindi,
        english_marks=english,
        maths_marks=maths,
        science_marks=science,
        social_marks=social

    )
    data.save()
    return redirect('/')
