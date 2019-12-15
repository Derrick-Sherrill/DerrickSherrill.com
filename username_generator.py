import requests
from random import randint

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"

r = requests.get(word_site)

txt = r.text
individual_words = txt.split()
print(individual_words)
random_number = randint(0, len(individual_words))
print(random_number)

print(individual_words[random_number] + str(random_number))
