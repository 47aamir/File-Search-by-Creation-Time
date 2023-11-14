import os
from datetime import datetime, timedelta
from time import sleep

try:
    print('Enter Duration i.e: -days=2, +minutes=60, -seconds=180 : ')
    print('Leading + is for more than and - is for less than')
    sleep(0.5)
    input_str = input()
    # Extracting the comparison operator and duration parts
    comparison_operator = input_str[0]
    duration_parts = input_str[1:].split('=')
    
    if comparison_operator not in ('-', '+'):
        raise ValueError("Invalid comparison operator. Please enter - or +")

    takeinputdir = input('Enter Path i.e c:\\Users\\ : \n')
    takeinputdir1 = takeinputdir.replace("\\", "\\\\")

    time_unit = duration_parts[0].strip()
    time_value = int(duration_parts[1].strip())

    now = datetime.now()
    check_duration = now - timedelta(**{time_unit: time_value})

    for root, dirs, files in os.walk(os.path.expanduser(takeinputdir1)):
        for file in files:
            file_path = os.path.join(root, file)
            ctime = datetime.fromtimestamp(os.path.getctime(file_path))
            
            # Check whether the duration is less than or more than based on user input
            if (comparison_operator == '+' and ctime < check_duration) or \
               (comparison_operator == '-' and ctime > check_duration):
                print(file_path)
except Exception as e:
    print(f"*Error*: {e}, please try again!")
else:
    print("Search Done")
