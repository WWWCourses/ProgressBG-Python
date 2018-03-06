'''
acad_to_astro_hours_with_vars.py
an example of too many variables in a program
TODO: upload in slides
'''

minutes_in_astro_hour = 60
minutes_in_acad_hour = 40
acad_course_hourse = 12

acad_hours_partida = acad_course_hourse/4

minutes_brakes_in_partida = acad_hours_partida * 20

minutes_in_a_course = acad_course_hourse * minutes_in_acad_hour + minutes_brakes_in_partida

course_in_astro_hourse = minutes_in_a_course / 60

print(course_in_astro_hourse)



