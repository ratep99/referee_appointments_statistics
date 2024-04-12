import requests
from bs4 import BeautifulSoup
from collections import Counter
import pandas as pd

def scrape_delegiranje(kolo):
    # Constructing the URL for the specified round
    url = f"https://fsris.org.rs/takmicenja/srpska-liga-istok/?delegiranje=1&kolo={kolo}&sezona=16#"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Finding all div elements with class "delegiranje-info" containing information about referees
    delegiranje_info_divs = soup.find_all('div', class_='delegiranje-info')

    # Lists to store the names of main referees, assistant referees, and fourth officials
    main_referee_names = []
    first_assistant_referee_names = []
    second_assistant_referee_names = []
    fourth_official_names = []

    for delegiranje_info in delegiranje_info_divs:
        # Finding all span elements inside the div with class "delegiranje-info"
        sudije_spans = delegiranje_info.find_all('span')
        for span in sudije_spans:
            # Extracting referee names
            sudija_info = span.text.strip()
            if sudija_info.startswith("Glavni sudija:"):
                main_referee_names.append(sudija_info.split(":")[1].strip())
            elif sudija_info.startswith("Pomoćni sudija 1:"):
                first_assistant_referee_names.append(sudija_info.split(":")[1].strip())
            elif sudija_info.startswith("Pomoćni sudija 2:"):
                second_assistant_referee_names.append(sudija_info.split(":")[1].strip())
            elif sudija_info.startswith("Četvrti sudija:"):
                fourth_official_names.append(sudija_info.split(":")[1].strip())

    # Creating DataFrames for main referees, first assistant referees, second assistant referees, and fourth officials
    main_referees_df = pd.DataFrame({'Ime i Prezime': main_referee_names})
    first_referees_df = pd.DataFrame({'Ime i Prezime': first_assistant_referee_names})
    second_referees_df = pd.DataFrame({'Ime i Prezime': second_assistant_referee_names})
    fourth_referees_df = pd.DataFrame({'Ime i Prezime': fourth_official_names})

    # Concatenating DataFrames for main referees and fourth officials, and for assistant referees
    referees_df = pd.concat([main_referees_df,fourth_referees_df],ignore_index=True)
    assistants_df = pd.concat([first_referees_df,second_referees_df],ignore_index=True)

    return referees_df,assistants_df

# Gathering data for specific rounds
target_rounds = [3867] + list(range(3872, 3886)) + list(range(4319, 4326))
referee_df = pd.DataFrame()
assistant_df = pd.DataFrame()

for kolo in target_rounds:
    main_referee_df, assistant_referee_df = scrape_delegiranje(kolo)
    referee_df = pd.concat([referee_df, main_referee_df], ignore_index=True)
    assistant_df = pd.concat([assistant_df, assistant_referee_df], ignore_index=True)

# Displaying unique names and their occurrences
unique_referees = referee_df['Ime i Prezime'].value_counts()
unique_assistants = assistant_df['Ime i Prezime'].value_counts()

print("Unique referee names:")
print(unique_referees)
print("\nUnique assistant referee names:")
print(unique_assistants)
