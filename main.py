from matching.games import HospitalResident
import preferences

def main():
    pm = preferences.PreferenceMaker()
    client_prefs = pm.getClientPreferences()
    member_prefs = pm.getMemberPreferences()
    member_caps = pm.getMemberCaps()

    game = HospitalResident.create_from_dictionaries(
        client_prefs, member_prefs, member_caps
    )

    matching = game.solve(optimal="resident")
    for item in matching.items():
        print(item)

    matched_clients = []
    for _, clients in matching.items():
        for client in clients:
            matched_clients.append(client.name)

    unmatched_clients = set(client_prefs.keys()) - set(matched_clients)

    if len(unmatched_clients) != 0:
        print(f"Some clients have gone unpaired: {unmatched_clients}")

if __name__ == "__main__":
    main()