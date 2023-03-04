import movie_data
from utils import get_rating, get_title, average_rating

def main():
    movies = movie_data.movies
    print(f'Total number of movies: {count_movies(movies)}')
    print(f'Average rating of movies: {average_rating(movies)}')
    print(f'Best movie: "{get_best_movie(movies)}"')
    print(f'Worst movie: "{get_worst_movie(movies)}"')

def count_movies(movies):
    return len(movies)

def get_best_movie(movies):
    best = max(movies, key=get_rating)
    return get_title(best)

def get_worst_movie(movies):
    worst = min(movies, key=get_rating)
    return get_title(worst)

if __name__ == '__main__':
    main()
