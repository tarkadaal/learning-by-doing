# Actor appearing in most movies
# Actor with best average rating
# Least popular genre in the 1980s
#
import movie_data
from collections import defaultdict

def main():
    print(f'Actor appearing in most movies: {get_popular_actor(movie_data.movies)}')
    print(f'Actor with best average rating: {get_actor_with_best_average_rating(movie_data.movies)}')
    print(f'Least popular genre in the 1980s: {get_least_popular_genre_in_1980s(movie_data.movies)}')

def get_popular_actor(movies):
    actor_count = {}
    for movie in movies:
        for actor in movie['actors']:
            actor_count[actor] = 1 + actor_count[actor] if actor in actor_count else 1
    return max(actor_count, key=actor_count.get)

def get_actor_with_best_average_rating(movies):
    actor_ratings = {}
    for movie in movies:
        for actor in movie['actors']:
            actor_ratings[actor] = actor_ratings[actor] + [movie['rating']] if actor in actor_ratings else [movie['rating']]
    actor_averages = {k: sum(v) / len(v) for k, v in actor_ratings.items()}
    return max(actor_averages, key=actor_averages.get)

def get_least_popular_genre_in_1980s_old(movies):
    eighties_genres= [x['genre'] for x in movies if 1979 < x['year'] < 1990]
    genre_count = {}
    for genre in eighties_genres:
        genre_count[genre] = 1 + genre_count[genre] if genre in genre_count else 1
    return min(genre_count, key=genre_count.get)

def get_least_popular_genre_in_1980s(movies):
    by_genre = pivot(movies, 'genre')
    by_genre = {k: [x for x in v if 1979 < x['year'] < 1990]  for k, v in by_genre.items()}
    print(by_genre['horror'])
    return min(by_genre, key=lambda x: len(by_genre[x]))

def pivot(movies, new_key):
    new_dict = defaultdict(list)
    for m in movies:
        new_dict[m[new_key]].append(m)
    return new_dict


if __name__ == '__main__':
    main()
