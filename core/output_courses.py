from .model_trainer import *
from .extract_classes import *

def output_course_results(courses_to_log_prob, list_of_eecs_courses):
    courses_names_to_display = list(dict(courses_to_log_prob).keys())[-5:] #courses we will show the user

    courses_to_difficulty = {courses_names_to_display[i]: list_of_eecs_courses[courses_names_to_display[i]][0] for i in range(0, 5)}
    courses_to_difficulty = sorted(courses_to_difficulty.items(), key=lambda item: item[1], reverse=True)
    courses_to_difficulty_printed = []
    for course in courses_to_difficulty:
        courses_to_difficulty_printed.append(course[0] + " (" + "%.2f" % (course[1]) + ")")

    courses_to_workload = {courses_names_to_display[i]: list_of_eecs_courses[courses_names_to_display[i]][1] for i in range(0, 5)}
    courses_to_workload = sorted(courses_to_workload.items(), key=lambda item: item[1])
    courses_to_workload_printed = []
    for course in courses_to_workload:
        courses_to_workload_printed.append(course[0] + " (" + "%.2f" % (course[1]) + ")")
    

    courses_names_to_display.reverse()
    return (courses_names_to_display, courses_to_difficulty_printed, courses_to_workload_printed)
