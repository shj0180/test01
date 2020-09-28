# encoding='utf-8'
from pywinauto.application import Application
import os,subprocess,psutil,signal,time,sys,pyautogui
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
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
    try:
        pids = psutil.pids()
        for pid in pids:
            p = psutil.Process(pid)
            process_name = p.name()
            # print(process_name, pid)
            name_list = get_process_name()
            for processname in name_list:
                if processname == process_name:
                    # os.kill(pid)
                    command = 'taskkill /F /IM %s'%pid
                    os.system(command)
    except Exception:
        pass

def start_moni():
    app_adress = r'C:\175撮合\sh\sh_moni.exe'
    aim_dir = os.path.dirname(app_adress)
    os.chdir(aim_dir)
    os.popen(app_adress.split('\\')[-1])

    time.sleep(1)
    app = Application().connect(path=app_adress)
    time.sleep(1)
    qd = app.window(class_name='WindowsForms10.Window.8.app.0.2bf8098_r11_ad1',title='上海模拟撮合').child_window(title="启动", auto_id="start_cl", control_type="System.Windows.Forms.Button")
    # qd.print_control_identifiers()
    qd.click()

def start_sjs_socket():
    app_adress_list = []
    with open('./CLIENT_LOCATION.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            if line == '\n' or 'moni' in line:
                pass
            else:
                app_adress = line.strip('\n')
                app_adress_list.append(app_adress)
                aim_dir = os.path.dirname(app_adress)
                os.chdir(aim_dir)
                os.popen(app_adress.split('\\')[-1])
    # print(app_adress_list)
    # app_adress_list = ['C:\\175撮合\\sz\\sjs_socket-CAT\\sjs_socket.exe', 'C:\\175撮合\\sz\\sjs_socket-INT\\sjs_socket.exe', 'C:\\175撮合\\sz\\sjs_socket-NM\\sjs_socket.exe', 'C:\\175撮合\\sz\\sjs_socket-NT\\sjs_socket.exe']
    for i in app_adress_list:
        app = Application().connect(path=i)
        Form1 = app.window(class_name='WindowsForms10.Window.8.app.0.9585cb_r11_ad1',title='Form1')
        Form1.Minimize()

    for i in app_adress_list:
        app = Application().connect(path=i)
        Form1 = app.window(class_name='WindowsForms10.Window.8.app.0.9585cb_r11_ad1', title='Form1')
        Form1.Restore()
        kq1 = app.window(class_name='WindowsForms10.Window.8.app.0.9585cb_r11_ad1',title='Form1').child_window(title="开启模拟撮合", auto_id="button1", control_type="System.Windows.Forms.Button")
        # kq1.print_control_identifiers()
        kq1.click()
        Server = app.window(class_name='WindowsForms10.Window.8.app.0.9585cb_r11_ad1',title='Server')
        # 

        ser1 = app.window(class_name='WindowsForms10.Window.8.app.0.9585cb_r11_ad1',title='Server').child_window(title="启动模拟撮合", auto_id="btn_start", control_type="System.Windows.Forms.Button")
        ser1.click()
        Server.Minimize()
        Form1.Minimize()


if __name__ == '__main__':

    stop()
    stop()
    stop()
    stop()

    start_sjs_socket()
    start_moni()

    # start()

