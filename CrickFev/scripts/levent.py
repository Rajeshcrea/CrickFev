import requests
import sys
import click
from bs4 import BeautifulSoup as BS


url = "http://www.espncricinfo.com/ci/engine/match/index.html?view=live"
r = requests.get(url)
soup = BS(r.text, "html.parser")
tableHeads = soup.find_all('div', {'class' : 'match-section-head'})
tableData = soup.find_all('section', {'class' : 'matches-day-block'})
team_matches = []

def getLiveEvents():
        print("\nEvents Going On Live Right Now")
        for ix in range(0, len(tableHeads)):
            print("\t" + str(ix+1) + ". " + str(tableHeads[ix].h2.text))

@click.command(help='Events Going On Live Right Now--(cricket)')

def main():
    click.echo("\n" + "*" * 100)
    click.echo("Welcome!")
    
    getLiveEvents()


