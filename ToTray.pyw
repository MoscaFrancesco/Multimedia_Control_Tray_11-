from infi.systray import SysTrayIcon
from pynput.keyboard import Controller, KeyCode
import time


keyboard = Controller()
startup_timer = 0.5
# --------------------------------- Previous --------------------------------- #
def Previous(bf):
    print("Previous")

    #uso un tasto virtuale, la lista è https://cherrytree.at/misc/vk.htm
    #il numero è il 177 che in decimale è B1

    keyboard.press(KeyCode.from_vk(0xB1))  # Play/Pause
    
IconPrev="Prev.ico"
menu_options = (("Previous", None, Previous),)
Previous_SysTray = SysTrayIcon(IconPrev, "Previous", menu_options)
Previous_SysTray.start()
time.sleep(startup_timer)

# -------------------------------- Play/Pause -------------------------------- #
def Pause(bf):
    print('Pausing/Resuming... ')

    #uso un tasto virtuale, la lista è https://cherrytree.at/misc/vk.htm
    # il numero è il 179 che in decimale è B3

    keyboard.press(KeyCode.from_vk(0xB3))  # Play/Pause
    
IconPause = "play-pause.ico"
menu_options = (("Pause", None, Pause),)
Pause_SysTray = SysTrayIcon(IconPause, "Pause", menu_options)
Pause_SysTray.start()
time.sleep(startup_timer)


# ----------------------------------- Next ----------------------------------- #
def Next(bf):
    print('Next... ')

    #uso un tasto virtuale, la lista è https://cherrytree.at/misc/vk.htm
    # il numero è il 176 che in decimale è B0
    keyboard.press(KeyCode.from_vk(0xB0))  # Play/Pause
    
IconNext = "Next.ico"
menu_options = (("Next", None, Next),)
Next_SysTray = SysTrayIcon(IconNext, "Next", menu_options)
Next_SysTray.start()


