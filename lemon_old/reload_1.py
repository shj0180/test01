# encoding='utf-8'
from pywinauto.application import Application
import os,subprocess,psutil,signal,time,sys
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)

def get_process_name():
    name_list = []
    with open('./CLIENT_LOCATION.txt','r',encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line =='\n':
                pass
            else:
                list = line.split(',')
                app_name = list[0].split('\\')[-1].strip('\n')
                # print(app_name)
                name_list.append(app_name)
    return name_list

def stop():
    pids = psutil.pids()
    try:
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            # print(process_name, pid)
            name_list = get_process_name()


            for processname in name_list:
                if processname == process_name:
                    # print(process_name, pid)
                    command = 'taskkill /F /IM %s'%pid
                    os.system(command)
    except Exception as e:
        print('except!!!:%s' % e)


def start():
    with open('./CLIENT_LOCATION.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        path_list = []
        for line in lines:
            if line == '\n':
                pass
            else:
                path_list.append(line.strip('\n').strip('\ufeff'))

        for p in path_list:
            print(p)
            aim_dir = os.path.dirname(p)
            # print(BASE_DIR)
            os.chdir(aim_dir)
            # print(p.split('\\')[-1])
            os.popen(p.split('\\')[-1])



if __name__ == '__main__':
    stop()
    stop()
    stop()
    stop()
    stop()
    stop()
    start()

