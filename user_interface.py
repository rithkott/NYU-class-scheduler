import json_parser as jp

def course_lister():
    print("Welcome, to begin building your schedule, add classes by following the directions below")
    main_course_list = []
    main_breaker = False
    while not main_breaker:

        subject = input("Enter your subject code: ")
        
        flag1 = True
        while flag1:
            class_list = jp.get_courses(subject)
            if class_list != None:
                flag1 = False
                break
            else:
                print("That subject code does not exist, please double check that you've typed it exactly as it appears in Albert.")
                subject = input("Enter your subject code: ")
        
        id_list = jp.get_course_ids(subject)
        
        print("Classes: ")
        for i in class_list:
            print(i)
        
        flag2 = True
        while flag2:
            course_id = input("Enter your course ID as it appears in the list above: ")
            course_id = course_id.upper()
            if course_id in id_list and (subject.upper(), course_id) not in main_course_list:
                main_course_list.append((subject.upper(), course_id))
                print(f"You have successfully added {subject.upper()} {course_id}")
                flag2 = False
            elif course_id in id_list and (subject.upper(), course_id) in main_course_list:
                print("You've already added that course to your schedule.")
                break
            else:
                print("That course ID does not exist. Please check that it matches an ID in the list above.")

        breaker1 = False
        flag3 = True
        while flag3:
            print("Enter C to add another class to your schedule. Enter D to generate your schedule")
            loop_break = input()
            if loop_break.upper() == 'C':
                flag3 = False
            elif loop_break.upper() == 'D':
                breaker1 = True
                flag3 = False
                main_breaker = True
            else:
                print("Invalid input")
    return main_course_list

