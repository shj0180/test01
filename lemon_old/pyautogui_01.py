import pyautogui
import threading


def do():
    # print('1')
    # while 1:
    t = '''sssss\nssss'''
    pyautogui.prompt()
    pyautogui.confirm(text=t,buttons=['OK', 'Cancel'])
    #     if xx == 'OK':
    #         continue
    #     else:
    #         break


t1 = threading.Thread(target=do)
# t2 = threading.Thread(target=do)
# t3 = threading.Thread(target=do)
t1.start()
# t2.start()
# t3.start()



