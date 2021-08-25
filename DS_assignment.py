input_file = open("1.in")
timetable_dict = {}
people_count = 0
line_counter = 0
start_time_key = 0
end_time = 0
points_min = 0
points_min_person = None
points_dict = {}

people_count = int(input_file.readline())
line_counter = line_counter + 1
for line in input_file:
    start_time_key, end_time = line.split()
    start_time_key = int(start_time_key)
    end_time = int(end_time)
    for start_time in range(start_time_key, end_time):
        if start_time in timetable_dict:
            timetable_dict[start_time] = []
        else :
            timetable_dict[start_time] = [line_counter]
    line_counter = line_counter + 1

for start_time_key in timetable_dict:
    if len(timetable_dict[start_time_key]) == 1:
        points_dict_key = timetable_dict[start_time_key][0]
        if points_dict_key in points_dict:
            points_dict[points_dict_key] = points_dict[points_dict_key] + 1
        else :
            points_dict[points_dict_key] = 1

for person in range(1,(people_count+1)):
    if person not in points_dict:
        points_min_person = person
        points_min = 0
        break
    else:
        if points_dict[person] < points_min or points_min_person == None:
            points_min = points_dict[person]
            points_min_person = person

coverage = len(timetable_dict)
overall_coverage = coverage - points_min
print(overall_coverage)

