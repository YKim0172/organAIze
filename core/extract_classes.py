from bs4 import BeautifulSoup
import requests
import pandas as pd
import os

def index_of_new_word(str):
    for i in range(0, len(str)):
        if (ord(str[i]) != 32 and ord(str[i]) != 10 and ord(str[i]) != 9 and ord(str[i]) != 13):
            #print(i)
            return i

def add_course_name(course_name, list_of_EECS_courses):
    final_course_name = ""
    #add the EECS part
    for i in range(0, 4):
        start_of_new_word = index_of_new_word(course_name)
        match i:
            case 0:
                final_course_name += (course_name[start_of_new_word: start_of_new_word + 4] + " ")
                course_name = course_name[start_of_new_word + 4:]
            case 1:
                final_course_name += (course_name[start_of_new_word: start_of_new_word + 3] + " ")
                course_name = course_name[start_of_new_word + 3:]
                #if course already inside EECS courses list
            case 2:
                final_course_name += (course_name[start_of_new_word: start_of_new_word + 1] + " ")
                course_name = course_name[start_of_new_word + 1:]
            case 3:
                long_course_name = course_name.strip()
                long_course_name = long_course_name.replace(",", "")
                long_course_name = long_course_name.replace("/ ", "")
                final_course_name += long_course_name
    #add course if already not in list
    if final_course_name not in list_of_EECS_courses: #do the statistics library stuff here
        data_for_current_class = pd.read_csv("core/course_stats/" + f"{final_course_name}.csv")
        print(final_course_name)
        list_of_EECS_courses[final_course_name] = (data_for_current_class["grade"].mean(), data_for_current_class["workload"].mean())

#page of ALL majors
#page_of_all_majors = requests.get("https://www.lsa.umich.edu/cg/cg_subjectlist.aspx?termArray=f_23_2460&cgtype=ug&allsections=true").text
#soup = BeautifulSoup(page_of_all_majors, 'lxml')
#table_of_majors = soup.find("table", class_ = "table table-striped table-condensed").tbody

#EECS courses exclusively
def extract_class_data():
    list_of_EECS_courses = {}
    page_number = 1
    while True:
        eecs_page = requests.get(f"https://www.lsa.umich.edu/cg/cg_results.aspx?termArray=f_23_2460&cgtype=ug&department=EECS&allsections=true&show=40&iPageNum={page_number}").text
        eecs_soup = BeautifulSoup(eecs_page, 'lxml')
        all_eecs_courses_on_page = eecs_soup.find_all("div", class_ = "row ClassRow ClassHyperlink result")
        all_eecs_courses_on_page_alt = eecs_soup.find_all("div", class_ = "row ClassRow ClassHyperlink resultalt")

        for course in all_eecs_courses_on_page:
            courseName = course.div.div.div.a.font.text
            add_course_name(courseName, list_of_EECS_courses)
        for course in all_eecs_courses_on_page_alt:
            courseName = course.div.div.div.a.font.text
            add_course_name(courseName, list_of_EECS_courses)
        #courses on the page have been added
        #check if next page exists
        link_to_next_page = eecs_soup.find("a", id = "contentMain_hlnkNextBtm")
        if (link_to_next_page == None):
            break
        else:
            page_number += 1
    return list_of_EECS_courses