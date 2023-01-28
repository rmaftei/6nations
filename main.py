import requests

website = "https://g9u7p6f6.ssl.hwcdn.net/api/custom/fixtureResult/season/22GUIN65?lang=en_GB"

def printTable(meciuri, default_spacing = '\t\t'):
    table = []

    for idx, meci in enumerate(meciuri):
        score = meci['score']
        score_teamA = score['teamA']
        score_teamB = score['teamB']

        htscore = meci['htscore']
        htscore_teamA = htscore['teamA']
        htscore_teamB = htscore['teamB']

        teams = meci['teams']
        teamA_name = teams['teamA']['name']
        teamB_name = teams['teamB']['name']
        
        datetime = meci['datetime_display']
        venue_name = meci['venue']['name']
        venue_location = meci['venue']['location']

        tabs = default_spacing
        
        if len(teamA_name) + len(str(idx + 1)) <= 6:
            tabs = default_spacing + '\t'
        
        table.append(f'{default_spacing}{datetime} {venue_name} ({venue_location})')
        table.append(f'{idx + 1} {teamA_name}{tabs}{score_teamA} - {score_teamB}\t\t\t{teamB_name}')
        table.append(f'{default_spacing}       ({htscore_teamA} - {htscore_teamB})')
        table.append('--------------------------------------------------------------')
    
    return '\n'.join(table)

if __name__ == '__main__':
    try:
        r = requests.get(website)
    except:
        print("Something went wrong when getting the data")

    meciuri = r.json()['data']

    print(printTable(meciuri))
