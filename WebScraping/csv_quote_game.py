from csv import DictReader
from random import choice

import requests
from bs4 import BeautifulSoup

BASE_URL = "http://quotes.toscrape.com"


def read_quotes(filename):
    with open(filename, "r") as file:
        csv_reader = DictReader(file)
        return list(csv_reader)


def start_game(quotes):
    quote = choice(quotes)
    remaining_quesses = 4
    print("Here's a quote: ")
    print(quote["text"])
    print(quote["author"])
    guess = ''
    while guess.lower() != quote['author'].lower() and remaining_quesses > 0:
        guess = input(f"Who said this quote? Guesses remaining: {remaining_quesses} ")
        if guess.lower() == quote['author'].lower():
            print("You Got It Right!")
            break
        remaining_quesses -= 1
        print_hint(quote, remaining_quesses)
    again = ""
    while again.lower() not in ('y', 'yes', 'n', 'no'):
        again = input("Would you like to play again (y/n)? ")
    if again.lower() in ("yes", "y"):
        return start_game(quotes)
    else:
        print("OK, Goodbye!")


def print_hint(quote, remaining_quesses):
    if remaining_quesses == 3:
        res = requests.get(f"{BASE_URL}{quote['bio-link']}")
        soup = BeautifulSoup(res.text, "html.parser")
        birth_date = soup.find(class_="author-born-date").get_text()
        birth_place = soup.find(class_="author-born-location").get_text()
        print(f"Here's a hint: The author was born in {birth_date} in {birth_place}")
    elif remaining_quesses == 2:
        print(f"Here's a hint: The author's first name starts with: {quote['author'][0]}")
    elif remaining_quesses == 1:
        last_initial = quote['author'].split(" ")[1][0]
        print(f"Here's a hint: The author's last name starts with: {last_initial}  ")
    else:
        print(f"Sorry you ran out of guesses. The answer was {quote['author']}")


quotes = read_quotes("quotes.csv")
start_game(quotes)
