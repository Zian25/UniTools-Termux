# Coding: UTF-8

import json
import os.path
import time
import src.settings
import src.core

cachedSettings = src.settings.Settings.getSettings()
langVars = src.settings.Language.getVars()

red = '\033[31m'
white = '\033[37m'
green = '\033[32m'
yellow = '\033[0;33m'


def listTools(option: int):
    space = " "*cachedSettings['menuSpace']
    tools = {
        1: "infogathering",
        2: "dos",
        3: "phishing",
        4: "exploitation",
        5: "bruteforce",
        6: "utils"
    }
    with open(f"src/tools/{tools[option]}.json", mode="r", encoding="utf-8") as tool:
        menu = json.load(tool)

    toolsLen = range(len(menu))
    availableTools = []
    while True:
        try:
            src.core.clear()
            for item in toolsLen:
                if os.path.exists(cachedSettings['path']+'/'+menu[item]['name']):
                    print(space + f"{green}{item}: {menu[item]['name']}{white}")
                else:
                    print(space+f"{item}: {menu[item]['name']}")
                availableTools.append(str(item))
            print(space+langVars['return']+"\n")
            choose = input(space+f"{langVars['input']}").lower()
            if choose == "x":
                return
            if choose == "all":
                # TODO
                pass
            if choose in availableTools:
                src.core.downloadTool(menu[int(choose)])
                pass

        except ValueError:
            src.core.clear()
            print(langVars['invalid'])
            time.sleep(cachedSettings['sleep'])

        except KeyboardInterrupt:
            src.core.clear()
            exit(1)








