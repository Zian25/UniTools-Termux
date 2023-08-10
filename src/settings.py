# Coding: UTF-8
import json


class Settings:
    @staticmethod
    def getSettings() -> object:
        with open("data/config/settings.json", mode="r", encoding="utf-8") as setting:
            settings = json.load(setting)
        return settings

    @staticmethod
    def setSettings(data: object) -> bool:
        try:
            with open("data/config/settings.json", mode="w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
                return True
        except:
            return False


class Language:
    path = None
    global cachedSettings
    cachedSettings = Settings.getSettings()

    @classmethod
    def available(cls) -> str:
        with open("data/lang/available.json", mode="r", encoding="utf-8") as data:
            cls.path = json.load(data)
            return cls.path

    @staticmethod
    def enum():
        return len(Language.available()["languages"]) - 1

    @staticmethod
    def listLanguages():
        available = Language.available()
        for counter, language in enumerate(available["languages"], start=0):
            print(" "* Settings.getSettings()['menuSpace'] + f"{counter}: {language['name']}")

    @staticmethod
    def setLanguage(number: int) -> bool:
        available = Language.available()
        available_len = len(available["languages"]) - 1

        if 0 <= number <= available_len:
            cachedSettings["language"] = number
            Settings.setSettings(cachedSettings)
            return True
        return False


    @staticmethod
    def getVars():
        with open("data/lang/available.json", mode="r", encoding="utf-8") as language_preset:
            language = json.load(language_preset)
        with open(f'{language["languages"][cachedSettings["language"]]["path"]}', encoding="utf-8", mode="r") as currentLang:
            return json.load(currentLang)
