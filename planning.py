import time, os

def check_script(script:str=None) -> str:
    if not os.path.exists(script):
        print(f'Скрипт {script} не обнаружен. Проверь правильность имени скрипта')
        script = None
    return script

def Checker(check_time:str=None, script:str=None):
    try:
       
        if check_time == None:print('Не обозначено время, необходимо добавить время в планировщик')
        if script == None:print('Не обозначен скрипт запуска')
        while True:
            
            search_script = check_script(script=script)
            if search_script == None:
                break
            if check_time == None or script == None:
                break

            current_time = time.strftime("%H:%M")
            if check_time == current_time:
                os.system(f'source venv/bin/activate && python3 {script}')
            print(f'Текущее время {current_time}. Задача запланирована на {check_time}')
            time.sleep(60)
            
    except KeyboardInterrupt:print('\nВыход из программы...')

Checker(check_time="9:00", script="y_comb.py")
