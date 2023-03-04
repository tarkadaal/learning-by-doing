# Actor appearing in most movies
# Actor with best average rating
# Least popular genre in the 1980s
#
import movie_data
from utils import pivot, pivot_ex, per_actor, average_rating, get_year

def main():
    popular_actor = get_popular_actor(movie_data.movies)
    print(f'Actor appearing in most movies: {popular_actor}')
    best_actor = get_actor_with_best_average_rating(movie_data.movies)
    print(f'Actor with best average rating: {best_actor}')
    least_popular_genre = get_least_popular_genre_in_1980s(movie_data.movies)
    print(f'Least popular genre in the 1980s: {least_popular_genre}')

def get_popular_actor(movies):
    by_actor = pivot_ex(movies, per_actor)
    return max(by_actor, key=lambda x: len(by_actor[x]))

def get_actor_with_best_average_rating(movies):
    by_actor = pivot_ex(movies, per_actor)
    average_rating_per_actor = {k: average_rating(v) for k, v in by_actor.items()}
    return max(average_rating_per_actor, key=average_rating_per_actor.get)

def get_least_popular_genre_in_1980s(movies):
    by_genre = pivot(movies, 'genre')
    by_genre = {k: movies_by_date(v, 1979, 1990) for k, v in by_genre.items()}
    return min(by_genre, key=lambda x: len(by_genre[x]))

def movies_by_date(movies, start, end):
    return [x for x in movies if start < get_year(x) < end]

if __name__ == '__main__':
    main()
