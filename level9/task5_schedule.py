schedule = [(9,11),(13,14),(15,16)]

def can_schedule(existing_meetings, new_meeting):
    new_start = new_meeting[0]
    new_end = new_meeting[1]

    can_schedule_check = True

    for meeting in existing_meetings:
        existing_start = meeting[0]
        existing_end = meeting[1]


        if new_start < existing_end and new_end > existing_start:
            can_schedule_check= False
            print("Накладається на : (", end="")
            print(f"{existing_start}: {existing_end})")


    if can_schedule_check: print("Вільне вікно")



can_schedule(schedule,(10,13))
can_schedule(schedule,(11,13))
