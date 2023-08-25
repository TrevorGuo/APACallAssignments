import fetchData
from enum import Enum

class PreferenceMaker:
    def __init__(self):
        DF = fetchData.DataFetcher()
        self.members = DF.getMembersList()
        self.clients = DF.getClientsList()
        self.englishProficiencyScore = {
            'Not at All': 3,
            'Not Well' : 2,
            'Well' : 1,
            'Very Well' : 0
        }
        self.clientLanguages = set()
        self.fillClientLanguages()
    
    def fillClientLanguages(self):
        for client in self.clients:
            for language in client.languages:
                self.clientLanguages.add(language)

    def getMemberPreferences(self):
        memberPreferences = {}
        for member in self.members:
            clientScores = []
            for client in self.clients:
                score = self.memberScoresClients(member, client)
                clientScores.append((client.id, score))
            clientScores.sort(key=lambda a:a[1], reverse=True)
            preference = []
            for client in clientScores:
                preference.append(client[0])
            memberPreferences[member.name] = preference
        return memberPreferences
    
    def memberScoresClients(self, member, client):
        score = 0
        for language in member.languages:
            if language in client.languages:
                score = score + 1
        if score == 0:
            score = score - self.englishProficiencyScore[client.englishProficiency]

        return score

    def getClientPreferences(self):
        clientPreferences = {}
        for client in self.clients:
            memberScores = []
            for member in self.members:
                score = self.clientScoresMembers(member, client)
                memberScores.append((member.name, score))
            memberScores.sort(key=lambda a:a[1], reverse=True)
            preference = []
            for member in memberScores:
                preference.append(member[0])
            clientPreferences[client.id] = preference
        return clientPreferences

    def clientScoresMembers(self, member, client):
        score = 0
        englishScore = self.englishProficiencyScore[client.englishProficiency]
        for language in client.languages:
            if language in member.languages:
                score = score + englishScore
        return score
    
    def getMemberCaps(self):
        memberCaps = {}

        num_members = len(self.members)
        num_clients = len(self.clients)

        num_calls = num_clients // num_members
        num_extra = num_clients % num_members

        memberImpact = []
        for member in self.members:
            score = 0
            for language in member.languages:
                if language in self.clientLanguages:
                    score = score + 1
            memberImpact.append((member.name , score))

        memberImpact.sort(key=lambda a:a[1], reverse=True)

        for member in memberImpact:
            if num_extra > 0:
                memberCaps[member[0]] = num_calls + 1
                num_extra = num_extra - 1
            else:
                memberCaps[member[0]] = num_calls

        return memberCaps