# Day of the week
MON = "monday"
TUE = "tuesday"
WED = "wednesday"
THU = "thursday"
FRI = "friday"
SAT = "saturday"
SUN = "sunday"

DAYS = [MON, TUE, WED, THU, FRI, SAT, SUN]

TRAINING_DAYS = [WED]
WEEKEND_DAYS = [SAT, SUN]
OTHER_DAYS = [MON, TUE, THU, FRI]

TRAINING_DAY_SCORE = 3
WEEKEND_DAY_SCORE = 2
OTHER_DAY_SCORE = 1


# GRADE
GOLD = "GOLD"
SILVER = "SILVER"
NORMAL = "NORMAL"

GRADE_CUTLINE = {
    GOLD: 50,
    SILVER: 30,
    NORMAL: 0
}

# SCORE

def get_score_of_day(day):
    if day in TRAINING_DAYS:
        return TRAINING_DAY_SCORE
    elif day in WEEKEND_DAYS:
        return WEEKEND_DAY_SCORE
    elif day in OTHER_DAYS:
        return OTHER_DAY_SCORE
    else:
        raise ValueError("It's not a day of week :", day)

# BONUS

TRAINING_DAY_BONUS_CONDITION = 10
TRAINING_DAY_BONUS_SCORE = 10
WEEKEND_BONUS_CONDITION = 10
WEEKEND_BONUS_SCORE = 10


member_dict = {} # member_name - id
member_num = 0

day_attendance_dicts = [{day: 0 for day in DAYS} for _ in range(100)]
names = [''] * 100
points = [0] * 100
grades = [0] * 100

def parse_data():
    args = get_args_from_file("attendance_weekday_500.txt")
    
    for member_name, day in args:
        update_member(member_name, day)

    for i in range(1, member_num + 1):
        points[i] += get_bonus_score(i)
        grades[i] = get_grade(i) 

def get_args_from_file(file_name):
    args = []
    try:
        with open(file_name, encoding='utf-8') as f:
            for _ in range(500):
                line = f.readline()
                if not line:
                    break
                parts = line.strip().split()
                if len(parts) == 2:
                    args.append((parts[0], parts[1]))

    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
    return args   

def update_member(member_name, day):
    if member_name not in member_dict:
        create_new_member(member_name)

    member_id = member_dict[member_name]
    points[member_id] += get_score_of_day(day)
    day_attendance_dicts[member_id][day] += 1

def create_new_member(member_name):
    global member_num
    member_num += 1
    member_dict[member_name] = member_num
    names[member_num] = member_name

def get_bonus_score(i):
    ret = 0
    if sum([day_attendance_dicts[i][day] for day in TRAINING_DAYS]) >= TRAINING_DAY_BONUS_CONDITION:
        ret += TRAINING_DAY_BONUS_SCORE
    if sum([day_attendance_dicts[i][day] for day in WEEKEND_DAYS]) >= WEEKEND_BONUS_CONDITION:
        ret += WEEKEND_BONUS_SCORE
    return ret

def get_grade(i):
    if points[i] >= GRADE_CUTLINE[GOLD]:
        return GOLD
    elif points[i] >= GRADE_CUTLINE[SILVER]:
        return SILVER
    elif points[i] >= GRADE_CUTLINE[NORMAL]:
        return NORMAL
    else:
        raise ValueError("NO available Grade :", i)

def is_removable_member(i):
    return (grades[i] == NORMAL) and (sum([day_attendance_dicts[i][day] for day in TRAINING_DAYS]) == 0) and (sum([day_attendance_dicts[i][day] for day in WEEKEND_DAYS]) == 0)


def print_result():
    for i in range(1, member_num + 1):
        print(f"NAME : {names[i]}, POINT : {points[i]}, GRADE : {grades[i]}")
        
    print("\nRemoved player")
    print("==============")
    for i in range(1, member_num + 1):
        if is_removable_member(i):
            print(names[i])

if __name__ == "__main__":
    parse_data()
    print_result()