# Serbian League Referees Scraper

This Python script scrapes data about referees and assistant referees from the Serbian League Istok website.

## Prerequisites

Before running the script, make sure you have Python installed on your system. You also need to install the following Python libraries:

- requests
- BeautifulSoup
- pandas

You can install these libraries using pip:

```bash
pip install requests beautifulsoup4 pandas
```

## Usage

1. Clone the repository to your local machine:

```bash
git clone <repository-url>
```

2. Navigate to the project directory:

```bash
cd serbian-league-referees-scraper
```

3. Run the script:

```bash
python scrape_referees.py
```

The script will scrape data for specific rounds of matches in the Serbian League Istok and display unique referee and assistant referee names along with their occurrences.
