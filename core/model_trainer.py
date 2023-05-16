import math
import csv
from collections import OrderedDict
from .extract_classes import *

def calculate_log_likelihood(course, word):
    if ((course,word) in class_label_word_to_num_posts_with_label_word):
        return math.log(class_label_word_to_num_posts_with_label_word[(course, word)] / class_label_to_num_posts[course])
    elif (word in unique_words_to_num_posts):
        return math.log(unique_words_to_num_posts[word] / num_prompts)
    else:
        return math.log(1 / num_prompts)

def predict(user_prompt, list_of_courses_taken):
    list_of_words = set(user_prompt.split())
    eecs_courses = extract_class_data()  #this is a map from course name to (grade, workload)
    courses_to_log_prob_score = {}
    index = 0
    for course in eecs_courses:
        if (list_of_courses_taken[index]):
            courses_to_log_prob_score[course] = -10000
        else:
            log_prob_score = math.log(class_label_to_num_posts[course] / num_prompts)  #log-prior
            for words in list_of_words:
                log_prob_score += calculate_log_likelihood(course, words)
            courses_to_log_prob_score[course] = log_prob_score
        index += 1
    return (courses_to_log_prob_score, eecs_courses)

#variables needed
num_prompts = 0
unique_words_to_num_posts = {}
class_label_to_num_posts = {}
class_label_word_to_num_posts_with_label_word = {}

#read in the csv file
with open("core/ML_training_data.csv", mode = "r") as file:
    csvFile = csv.reader(file)
    for user_request in csvFile:
        class_label = user_request[0]
        user_question = user_request[1]
        num_prompts += 1
        if (class_label not in class_label_to_num_posts):
            class_label_to_num_posts[class_label] = 1
        else:
            class_label_to_num_posts[class_label] += 1
        #split the string into its words
        user_question = user_question.lower()
        unique_words = set(user_question.split()) #unique words in user question
        for word in unique_words:
            if (word not in unique_words_to_num_posts):
                unique_words_to_num_posts[word] = 1
            else:
                unique_words_to_num_posts[word] = unique_words_to_num_posts[word] + 1
            if ((class_label, word) not in class_label_word_to_num_posts_with_label_word):
                class_label_word_to_num_posts_with_label_word[(class_label, word)] = 1
            else:
                class_label_word_to_num_posts_with_label_word[(class_label, word)] += 1