from movie_data import movies
from utils import get_actors, get_title, get_rating

def main():
    bad_actors = set(["Matthew Broderick"])
    good_actors = set(["Judd Nelson"])
    for m in movies:
        if "Judd Nelson" in get_actors(m): 
            for a in get_actors(m):
                good_actors.add(a)

    def adjusted_rating(movie):
        rating = get_rating(movie)
        actors = set(get_actors(movie))
        rating += 1 if good_actors.intersection(actors) else 0
        rating -= 1 if bad_actors.intersection(actors) else 0
        return rating

    ally_sheedy_movies = [m for m in movies if "Ally Sheedy" in get_actors(m)]
    adjusted = {get_title(m): adjusted_rating(m) for m in ally_sheedy_movies}
    print(max(adjusted, key=adjusted.get))


if __name__ == "__main__":
    main()
