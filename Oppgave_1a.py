class Films:
    def __init__(self, filmtittel, utgivelsesår, score):
        self.filmtittel = filmtittel
        self.utgivelsesår = utgivelsesår
        self.score = score


inception = Films("Inception", 2010, 8.8)
the_martian = Films("The Martian", 2015, 8.0)
joker = Films("Joker", 2019, 8.4)

print(f"{inception.filmtittel} was released in {inception.utgivelsesår} and currently has a score of {inception.score}")
print(f"{the_martian.filmtittel} was released in {the_martian.utgivelsesår} and currently has a score of {the_martian.score}")
print(f"{joker.filmtittel} was released in {joker.utgivelsesår} and currently has a score of {joker.score}")