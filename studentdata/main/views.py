from django.shortcuts import render
from django.http import HttpResponse

from accounts.models import Profile
from courses.models import Course



def HomeView(request):
	#total_students = len(Profile.objects.all())
	total_students = Profile.objects.count()
	total_courses = Course.objects.count()
	
	output = {
		"total_students": total_students,
		"total_courses": total_courses
	}
	return render(request, "index.html", output)

def StudentView(request):
	student_name =Profile.objects.all()
	
	
		
    
	return render(request, "student.html", {'students':student_name})


def CourseView(request):
	course_list =Course.objects.all()
	return render(request, "course.html", {'courses':course_list})