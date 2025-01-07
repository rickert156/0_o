import time, os

def Checker(check_time:str=None, script:str=None):
    while True:
        current_time = time.strftime("%H:%M")
        if check_time ==  current_time:
            os.system(f'source venv/bin/activate && python3 {script}')
        time.sleep(60)


Checker(check_time="9:00", script="y_comb.py") 
