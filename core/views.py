from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from members.forms import *
from members.models import *
from .model_trainer import *
from .output_courses import *

context = {}
# Create your views here.
def homepage(request):
    return render(request, 'core/home.html')

def main_page(request):
    if request.method == "POST":
        print("MADE IT HERE")
        whatUserWant = request.POST["USERTEXT"]
        #array of booleans indicating whether student took course
        list_of_courses_taken = [request.user.student.taken_EECS110, 
                                request.user.student.taken_EECS183, 
                                request.user.student.taken_EECS201, 
                                request.user.student.taken_EECS203, 
                                request.user.student.taken_EECS215, 
                                request.user.student.taken_EECS216, 
                                request.user.student.taken_EECS270, 
                                request.user.student.taken_EECS280, 
                                request.user.student.taken_EECS281, 
                                request.user.student.taken_EECS298, 
                                request.user.student.taken_EECS301, 
                                request.user.student.taken_EECS312, 
                                request.user.student.taken_EECS320, 
                                request.user.student.taken_EECS200, 
                                request.user.student.taken_EECS230, 
                                request.user.student.taken_EECS300, 
                                request.user.student.taken_EECS311, 
                                request.user.student.taken_EECS314, 
                                request.user.student.taken_EECS330, 
                                request.user.student.taken_EECS334, 
                                request.user.student.taken_EECS370, 
                                request.user.student.taken_EECS376, 
                                request.user.student.taken_EECS388, 
                                request.user.student.taken_EECS402, 
                                request.user.student.taken_EECS411, 
                                request.user.student.taken_EECS414, 
                                request.user.student.taken_EECS423, 
                                request.user.student.taken_EECS428, 
                                request.user.student.taken_EECS435, 
                                request.user.student.taken_EECS441, 
                                request.user.student.taken_EECS442, 
                                request.user.student.taken_EECS445, 
                                request.user.student.taken_EECS453, 
                                request.user.student.taken_EECS351, 
                                request.user.student.taken_EECS373, 
                                request.user.student.taken_EECS399, 
                                request.user.student.taken_EECS409, 
                                request.user.student.taken_EECS413, 
                                request.user.student.taken_EECS421, 
                                request.user.student.taken_EECS427, 
                                request.user.student.taken_EECS434, 
                                request.user.student.taken_EECS443, 
                                request.user.student.taken_EECS452, 
                                request.user.student.taken_EECS455, 
                                request.user.student.taken_EECS458, 
                                request.user.student.taken_EECS461, 
                                request.user.student.taken_EECS464, 
                                request.user.student.taken_EECS467, 
                                request.user.student.taken_EECS471, 
                                request.user.student.taken_EECS475, 
                                request.user.student.taken_EECS482, 
                                request.user.student.taken_EECS484, 
                                request.user.student.taken_EECS485, 
                                request.user.student.taken_EECS487, 
                                request.user.student.taken_EECS490, 
                                request.user.student.taken_EECS492, 
                                request.user.student.taken_EECS494, 
                                request.user.student.taken_EECS496, 
                                request.user.student.taken_EECS497, 
                                request.user.student.taken_EECS498, 
                                request.user.student.taken_EECS460, 
                                request.user.student.taken_EECS463, 
                                request.user.student.taken_EECS465, 
                                request.user.student.taken_EECS470, 
                                request.user.student.taken_EECS473, 
                                request.user.student.taken_EECS477, 
                                request.user.student.taken_EECS483, 
                                request.user.student.taken_EECS489, 
                                request.user.student.taken_EECS491, 
                                request.user.student.taken_EECS495, 
                                request.user.student.taken_EECS501, 
                                request.user.student.taken_EECS517, 
                                request.user.student.taken_EECS523, 
                                request.user.student.taken_EECS540, 
                                request.user.student.taken_EECS544, 
                                request.user.student.taken_EECS553, 
                                request.user.student.taken_EECS558, 
                                request.user.student.taken_EECS561, 
                                request.user.student.taken_EECS564, 
                                request.user.student.taken_EECS575, 
                                request.user.student.taken_EECS584, 
                                request.user.student.taken_EECS595, 
                                request.user.student.taken_EECS598, 
                                request.user.student.taken_EECS499, 
                                request.user.student.taken_EECS507, 
                                request.user.student.taken_EECS520, 
                                request.user.student.taken_EECS530, 
                                request.user.student.taken_EECS542, 
                                request.user.student.taken_EECS551, 
                                request.user.student.taken_EECS554, 
                                request.user.student.taken_EECS560, 
                                request.user.student.taken_EECS563, 
                                request.user.student.taken_EECS574, 
                                request.user.student.taken_EECS582, 
                                request.user.student.taken_EECS587, 
                                request.user.student.taken_EECS599, 
                                request.user.student.taken_EECS628]

        courses_to_log_prob_eecs_courses = predict(whatUserWant, list_of_courses_taken)
        sorted_courses_to_log_prob = sorted(courses_to_log_prob_eecs_courses[0].items(), key=lambda item: item[1])
        print(sorted_courses_to_log_prob)
        #use this tuple to print the 3 columns in mainpage
        tuple_of_courses_to_print = output_course_results(sorted_courses_to_log_prob, courses_to_log_prob_eecs_courses[1])
        context = {
            'courses_by_relevancy': tuple_of_courses_to_print[0],
            'courses_by_gpa': tuple_of_courses_to_print[1],
            'courses_by_hours': tuple_of_courses_to_print[2],
        }
        print(tuple_of_courses_to_print[0])
        return render(request, 'core/mainpage.html', context)
    else:
        context = {}

    return render(request, 'core/mainpage.html', context)