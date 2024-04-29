# coding: UTF-8
import sys
if sys.version_info[0] < 3:
    print("Python 2 is not supported, use Python 3!")
    exit(1)
import os.path
import time

import src.core
from src.settings import Settings, Language
from src.core import clear, banner, updateUTX, changeSettings
from src.manager import listTools


def main():
    cachedSettings = Settings.getSettings()
    langVar = Language.getVars()
    options = langVar["options"]
    menuSpace = cachedSettings['menuSpace']

    while True:
        try:
            clear()
            banner()
            print("\n")

            for index, item in enumerate(options, start=1):
                print(" " * menuSpace + f"{item['display']}")

            print("\n")
            choose = input(" " * menuSpace + langVar['input'])

            if choose in ["0", "00"]:
                clear()
                exit(0)
            elif choose in ["1", "2", "3", "4", "5", "6"]:
                listTools(int(choose))

            elif choose == "7":
                clear()
                changeSettings()

        except ValueError:
            clear()
            print(langVar['invalid'])
            time.sleep(cachedSettings['sleep'])

        except KeyboardInterrupt:
            clear()
            exit(1)


if __name__ == '__main__':
    cachedSettings = Settings.getSettings()
    if cachedSettings['language'] not in range(src.settings.Language.enum()):
        src.core.setLanguageInput()
        src.core.restart_program()

    if cachedSettings['path'] is None or not os.path.exists(cachedSettings['path']):
        cachedSettings['path'] = os.path.expanduser('~')
        Settings.setSettings(cachedSettings)
        src.core.restart_program()

    if cachedSettings["auto-update"] and not cachedSettings["debug"]:
        clear()
        updateUTX()
        
    main()
