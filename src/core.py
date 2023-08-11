# Coding: UTF-8
import sys
import os
import subprocess
import time
import json
import src.settings

cachedSettings = src.settings.Settings.getSettings()
cachedLang = src.settings.Language()
getVars = cachedLang.getVars()

red = '\033[31m'
white = '\033[37m'
green = '\033[32m'
yellow = '\033[0;33m'


def space() -> str:
    return " " * cachedSettings['menuSpace']


def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)
    curdir = os.getcwd()


def getVersion():
    with open("data/config/version.json") as version_preset:
        return json.load(version_preset)['version']


def banner():
    print("\n")
    print("                    #     # ####### #     # ")
    print("                    #     #    #     #   #  ")
    print("                    #     #    #      # #   ")
    print("                    #     #    #       #    ")
    print("                    #     #    #      # #   ")
    print("                    #     #    #     #   #  ")
    print(f"                     #####     #    #     #   v{getVersion()}")


def error(description, fatal=False, restart=False):
    print(description)
    if fatal:
        exit(1)
    if restart:
        restart_program()


def updateUTX():
    subprocess.run(["git pull"], shell=True)


def updateTermux():
    subprocess.run(["pkg", "update", "-y"], shell=True)
    subprocess.run(["pkg", "upgrade", "-y"], shell=True)


def setLanguageInput():
    try:
        src.core.clear()
        print(space() + "Please select a language\n")
        cachedLang.listLanguages()
        choose = int(input(space() + getVars['input']))
        if choose <= cachedLang.enum():
            cachedSettings['language'] = choose
            src.settings.Settings.setSettings(cachedSettings)
        else:
            setLanguageInput()
    except:
        setLanguageInput()


def downloadTool(toolObj: object):
    name = toolObj['name']
    url = toolObj['url']
    src.core.clear()
    subprocess.run(["git", "clone", url], cwd=cachedSettings['path'])
    src.core.clear()
    print(space() + f"{name} {getVars['downloadSuccess']} {cachedSettings['path']}")
    time.sleep(cachedSettings['sleep'])
    src.core.clear()


def changeSettings():
    keys = list(cachedSettings.keys())
    values = list(cachedSettings.values())
    available = len(keys)
    changes = 0

    while True:
        try:
            src.core.clear()
            print(f"\n{space()}{red}{getVars['warningConfig']}{white}\n")
            cachedLang.listLanguages()
            print("\n")

            for i, key in enumerate(keys):
                print(space() + f"[{i}] {key}: {values[i]}")

            if changes >= 1:
                print(space() + f"[R] Restart")
                print(f"{space()}{yellow}{getVars['restart']}{white}")

            print(space() + getVars['return'] + "\n")
            choose = input(space() + getVars['input']).lower()

            if choose == "x":
                return
            if choose == "r":
                src.core.restart_program()
            if choose.isdigit():
                choice = int(choose)
                if 0 <= choice < available:
                    key = keys[choice]
                    value = values[choice]
                    if key.lower() in ["language", "menuSpace", "sleep"]:
                        new_value = int(input(space() + getVars['inputSet'] + f"{key}: "))
                        cachedSettings[key] = new_value
                        src.settings.Settings.setSettings(cachedSettings)

                    elif key.lower() in ["auto-update", "debug", "preferGit"]:
                        new_value_str = input(space() + getVars['inputSet'] + f"{key}: ")
                        new_value = new_value_str.lower() == "true"
                        cachedSettings[key] = new_value
                        src.settings.Settings.setSettings(cachedSettings)

                    elif key.lower() in ["path"]:
                        new_value = input(space() + getVars['inputSet'] + f"{key}: ")
                        if os.path.exists(new_value):
                            cachedSettings[key] = new_value
                            src.settings.Settings.setSettings(cachedSettings)

                    changes += 1

        except (ValueError, IndexError):
            src.core.clear()
            print(getVars['invalid'])
            time.sleep(cachedSettings['sleep'])

        except KeyboardInterrupt:
            src.core.clear()
            return


def clear():
    subprocess.run(["clear"], shell=True)
