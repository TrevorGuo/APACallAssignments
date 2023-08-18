from enum import Enum

class Member:
    def __init__(self, name):
        self.name = name
        self.languages = set()
        self.clients = []

    def __str__(self):
        return f"{self.name}: {', '.join(list(self.languages))}"
    
    def addLanguage(self, language):
        self.languages.add(language)
    

class Client:
    def __init__(self, id, englishProficiency):
        self.id = id
        self.englishProficiency = englishProficiency
        self.languages = set()
    def __str__(self):
        return f"Client {self.id}:\n\tEnglish Level: {self.englishProficiency}\n\tLanguages: {', '.join(list(self.languages))}"
    def addLanguage(self, language):
        self.languages.add(language)
