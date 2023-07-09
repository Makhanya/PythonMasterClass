from pyfiglet import figlet_format
from termcolor import colored
from requests import get
from random import choice

print(colored(figlet_format("DAD Jokes 2000"), color="red"))
url = "https://icanhazdadjoke.com/search"
key_word = input("Let me tell your a joke! Give me a topic: ")
response = get(
    url,
    headers={"Accept": "application/json"},
    params={"term": key_word}
).json()

# print(
#     f"I; ve got {response['limit']} about {key_word}. Here's one: \n {response['results']}")

num_jokes = response['total_jokes']
results = response["results"]
if num_jokes > 1:
    print(f"I found {num_jokes} about {key_word}. Here's one:")
    print(choice(results)["joke"])
elif num_jokes == 1:
    print(f"I found one joke about {key_word}")
    print(results[0]["joke"])
else:
    print(f"Sorry, couldn't find a joke with your term: {key_word}")
