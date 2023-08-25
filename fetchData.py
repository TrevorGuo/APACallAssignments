import pandas as pd
import re
import classes
import os

class DataFetcher:
    def __init__(self):
        print(os.getcwd())
        # self.df = pd.read_csv('./Desktop/HealthFairData.csv')

    def getMembersList(self):
        df_members = self.df[['CR', 'Language Skills']].dropna()
        members = []

        for member, languages in df_members.itertuples(index=False):
            newMember = classes.Member(member.strip())
            # for language in languages:
            #     print(language)
            for language in re.split(', |; ', languages):
                newMember.addLanguage(language.strip()) 
            members.append(newMember)

        return members
    
    def getClientsList(self):
        df_clients = self.df[['Client ID', 'English Level', 'Preferred Languages']]
        clients = []

        for clientID, englishProficiency, languages in df_clients.itertuples(index=False):
            newClient = classes.Client(clientID, englishProficiency)
            if isinstance(languages, float):
                clients.append(newClient)
                continue
            for language in languages.split():
                if language != 'Other':
                    newClient.addLanguage(language)
            clients.append(newClient)

        return clients




