import json_parser as jp
import json
import datetime
from datetime import date
import user_interface as ui
from pprint import pprint
import itertools

def permutation_input():
    course_list = ui.course_lister()
    full_list = []
    print()
    print("Finding all course sections...")
    for i in course_list:
        codes_list = []    
        course_data = jp.get_course_data(i[0], i[1])
        section_codes = jp.get_section_codes(course_data[0])
        for j in section_codes:
            time_start = jp.get_lecture_start_time(course_data[1][0], course_data[1][1], j)
            time_end = jp.get_lecture_end_time(course_data[1][0], course_data[1][1], j, time_start)
            days = jp.get_lecture_days(course_data[1][0], course_data[1][1], j)
            registration_numbers = jp.get_registration_numbers(course_data[1][0], course_data[1][1], j)
            codes_list.append([course_data[1][0], course_data[1][1], j, time_start, time_end, days, registration_numbers])
        full_list.append(codes_list)
    return full_list

def preferences_filter(earliest_time, latest_time, main_list):
    print("Filtering preferences...")
    for i in main_list:
        for j in i:
            start_time = jp.get_lecture_start_time(j[0], j[1], j[2])
            end_time = jp.get_lecture_end_time(j[0], j[1], j[2], start_time)
            status = jp.get_status(j[0], j[1], j[2])
            if status == "Cancelled":
                i.remove(j)
            elif start_time < earliest_time:
                i.remove(j)
            elif end_time > latest_time:
                i.remove(j)
    return main_list

def permutation_output():
    input = permutation_input()
    time1 = datetime.time(8)
    time2 = datetime.time(20)
    datetime1 = datetime.datetime.combine(date.today(), time1)
    datetime2 = datetime.datetime.combine(date.today(), time2)
    filtered_input = preferences_filter(datetime1, datetime2, input)
    print("Calculating all course permutations...")
    permutations = list(itertools.product(*filtered_input))
    print(f"{len(permutations)} total permutations found")
    return permutations

def combinations_output(input):
    print("Rejecting course overlap...")
    combinations_dict = {}
    count = -1
    for i in input:
        count += 1
        combinations = list(itertools.combinations(i, 2))
        combinations_dict[count] = combinations
    return combinations_dict

def course_overlap_rejection(combinations_dict):
    final_dict = {}
    count = -1
    for i in combinations_dict:
        count+=1
        for j in combinations_dict[i]:
            flag = True
            time_start1 = j[0][3]

            time_start2 = j[1][3]

            time_end1 = j[0][4]

            time_end2 = j[1][4]

            days_meet1 = j[0][5]

            days_meet2 = j[1][5]


            if jp.days_overlap(days_meet1, days_meet2):
                if time_start2 >= time_start1 and time_start2 <= time_end1:
                    flag = False
                    break
                elif time_start1 >= time_start2 and time_start1 <= time_end2:
                    flag = False
                    break

        if not flag:
            continue
        else:
            final_dict[count] = combinations_dict[i]

    return final_dict

def main():
    permutation_list = permutation_output()
    valid_combos = combinations_output(permutation_list)
    overlap_filtered = course_overlap_rejection(valid_combos)
    count = -1
    print("Cleaning up schedule output")
    all_permutations = {}
    for i in overlap_filtered.keys():
        count+=1
        all_permutations[count] = permutation_list[i]
    pprint(all_permutations)
    if len(all_permutations) > 0:
        print(f"There are {len(all_permutations)} ways to arrange your schedule given your preferences")
    else:
        print("There are no schedules available, try expanding your search parameters")

main()



