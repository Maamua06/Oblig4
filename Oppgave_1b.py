class Films:
    def __init__(self, filmtittel, utgivelsesår, score):
        self.filmtittel = filmtittel
        self.utgivelsesår = utgivelsesår
        self.score = score

    def print_film(self):
        print(f"{self.filmtittel} was released in {self.utgivelsesår} and currently has a score of {self.score}")



inception = Films("Inception", 2010, 8.8)
the_martian = Films("The Martian", 2015, 8.0)
joker = Films("Joker", 2019, 8.4)

inception.print_film()
the_martian.print_film()
joker.print_film()