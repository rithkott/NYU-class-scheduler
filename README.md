# NYU-class-scheduler
An automatic class schedule generator for NYU meant to facilitate the process of signing up for classes

This is my first project, I made it right after I finished taking Intro to Programming because I came across a cool API by user A1Liu that tracked NYU's course offerings.
I wanted to make something that was challenging but would also solve a real problem (NYU Albert's time-consuming manual course selection)

The code is disorganized, the runtime is abysmal, and the algorithm is highly inefficient, but it was my first personal project and it does something cool. The only reason I haven't fixed it is that the API is no longer updated

THE API IS NO LONGER UPDATED, SO THIS PROGRAM NO LONGER WORKS FOR FUTURE SEMESTERS (Past Fall 2023)
However, it still works on past semesters if you want to check if your schedule could have been better.


How to use:
  - Go into json_generator.py and change the term to the term you wish to check using the first 2 letters of the season followed by the year (ex. sp2023, fa2019)
  - Run user_interface.py and follow the prompts, adding all the classes you need to take
  - When asked for the course code, enter the letters only and not the class number (ex. MATH-UA, ACCT-UB, EG-UY)
  - Find your class in the list that comes up and enter the number (Don't enter the number from memory, the API sometimes has them listed a bit differently)
  - Enter the earliest and latest hour you would like a class in 24 hour time (ex. 10 for 10:00am or 16 for 4:00pm)
  - The valid class schedules will print into the terminal (The API broke before I could implement any frontend T_T)
  - If no schedules are found, increase your time range and try again. (Remember the earliest classes start at 8am (8) and the latest classes end at 9pm (21))


How the scheduling algorithm works:
  - The program pulls all the sections of the classes you entered from the API, including labs and recitations as well
  - It then generates every permutation of sections you could sign up for (assuming 1 section from each class + labs and recitations)
  - The program checks if the classes occur on the same days, and if they do it checks if the class times overlap
  - It rejects every permutation with an overlap and prints the ones that are valid
  - This is a very brute-force algorithm, but its what I could think of at the time, and the runtime barely matters here because most people have <6 classes


Limitations:
  - If a class has both recitations and labs the program crashes, this is due to some disorganization on the API's side that I could not solve for
  - Most science/engineering classes crash the program because of this
  - The program will generate a valid schedule even if classes are 5 minutes apart but on different campuses, you should always manually check if the schedule works for you.
  - I never got around to adding campus filtering or integrating it with a Rate my Professor API as I had planned


If anyone wants to continue my work and adapt this code to a different API or take inspiration from the scheduling algorithm feel free to do so.

Please shoot me an email or Instagram DM if you do because I would be interested to see it. Contact Info is in my profile.
