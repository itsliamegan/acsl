distances = [450, 140, 125, 365, 250, 160, 380, 235, 320]

def get_distance_between(first_point, second_point):
    first_index = ord(first_point.upper()) - 65
    second_index = ord(second_point.upper()) - 65
    distances_between_connecting_points = distances[first_index:second_index]
    distance = sum(distances_between_connecting_points)

    return distance

def get_time_difference(first_time, second_time):
    if first_time > 12 and second_time < 12:
        second_time += 24

    difference = second_time - first_time

    return difference

def convert_to_24h_time(hour, meridian):
    if meridian.upper() == 'PM' and hour != 12:
        return hour + 12

    return hour

def format_time_from_decimal(time):
    hours = int(time)
    minutes = round((time - int(time)) * 60)

    if minutes < 10:
        minutes = f"0{minutes}"

    formatted = f"{hours}:{minutes}"

    return formatted

def get_time_until_meeting(distance, first_speed, second_speed, time_difference):
    return (distance + second_speed * time_difference) / (first_speed + second_speed)

for i in range(5):
    input_line = input().split(", ")
    first_point = input_line[0]
    second_point = input_line[1]
    first_hour = int(input_line[2])
    first_meridian = input_line[3]
    second_hour = int(input_line[4])
    second_meridian = input_line[5]
    first_speed = int(input_line[6])
    second_speed = int(input_line[7])

    first_time = convert_to_24h_time(first_hour, first_meridian)
    second_time = convert_to_24h_time(second_hour, second_meridian)

    distance = get_distance_between(first_point, second_point)
    time_difference = get_time_difference(first_time, second_time)
    time_until_meeting = get_time_until_meeting(distance, first_speed, second_speed, time_difference)
    formatted_time_until_meeting = format_time_from_decimal(time_until_meeting)

    print(formatted_time_until_meeting)

