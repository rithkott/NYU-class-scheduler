#import json
from json_generator import generate_json
import datetime
from datetime import date
import pandas as pd

#Retrieves a list of all sections and data for a given course
def get_subject_data(subject):
    subject_file_name = subject  + '.json'
    master_list = generate_json(subject)
    return master_list

def get_courses(subject):
    master_list = get_subject_data(subject)
    course_list = []
    
    try:
        if master_list["status"] == 400:
            return None
    except TypeError:

        for i in master_list:
            course_id = i["deptCourseId"]
            course_name = i["name"]
            course = course_id + " - " + course_name
            course_list.append(course)
        
        return course_list

def get_course_ids(subject):
    master_list = get_subject_data(subject)
    course_id_list = []
    
    for i in master_list:
        course_id = i["deptCourseId"]
        course_id_list.append(course_id)
    
    return course_id_list


def get_course_data(subject, course_id):
    
    master_list = generate_json(subject)
    course_file_name = subject + '_' + course_id + '.json'

    for i in master_list:
        if i["deptCourseId"] == course_id:
           
            sections = i["sections"]
            
#            with open(course_file_name, 'w') as course_file:
#                json.dump(sections, course_file, indent = 4)
            
            return (sections, (subject, course_id))

#Retrieves list of section codes
def get_section_codes(course_data):
    section_list = []
    
    for i in course_data:
        section_list.append(i["code"])
    
    return section_list

def get_registration_numbers(subject, course_id, section_code):
    section = get_section_data(subject, course_id, section_code)
    return section["registrationNumber"]

def get_section_data(subject, course_id, section_code):
    sections = get_course_data(subject, course_id)
    
    for i in sections[0]:
        if i["code"] == section_code:
            return i

#Retrieves a list of instructors for a given section
def get_instructors(subject, course_id, section_code):
    section = get_section_data(subject, course_id, section_code)
    return section["instructors"]

def get_status(subject, course_id, section_code):
    section = get_section_data(subject, course_id, section_code)
    return section["status"]

def get_campus(subject, course_id, section_code):
    section = get_section_data(subject, course_id, section_code)
    return section["campus"]

def get_lecture_days(subject, course_id, section_code):
    first_meeting_dates = []
    meeting_days = []  #Stores days that a class meets 1-5 (Monday-Friday)
    sections = get_section_data(subject, course_id, section_code)
    meetings = sections["meetings"]
    
    for i in meetings:
        date_time = i["beginDateLocal"]
        full_date = date_time[:10]
        first_meeting_dates.append(full_date)
   
    for i in first_meeting_dates:
        date = pd.Timestamp(i)
        day = date.day_name()
        meeting_days.append(day)
    
    return meeting_days


def get_lecture_start_time(subject, course_id, section_code):
    sections = get_section_data(subject, course_id, section_code)
    meetings = sections["meetings"]
    if len(meetings) == 0:
        return datetime.time(7)
    else:
        meeting = meetings[0]
    datetime_string = meeting["beginDateLocal"]

    time_string = datetime_string[11:16]
    time_list = time_string.split(':')                 
    
    if int(time_list[0]) < 8:
        hours = (int(time_list[0])) + 12
    else:
        hours = int(time_list[0])
    
    minutes = int(time_list[1])
    class_time = datetime.time(hours, minutes)
    start_time = datetime.datetime.combine(date.today(), class_time)
    return start_time

def get_lecture_end_time(subject, course_id, section_code, start_time):
    
    sections = get_section_data(subject, course_id, section_code)
    meetings = sections["meetings"]
    if len(meetings) == 0:
        return datetime.time(20)
    else:
        meeting = meetings[0]
    duration = meeting["minutesDuration"]
    
    end_time = start_time + datetime.timedelta(minutes=duration)

    return end_time

def days_overlap(days1, days2):
    result = False
    for x in days1:
        for y in days2:
            if x == y:
                result = True
                return result
    return result