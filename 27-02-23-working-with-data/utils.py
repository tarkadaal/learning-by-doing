from collections import defaultdict

def get_title(movie):
    return movie['title']

def get_actors(movie):
    return movie['actors']

def get_year(movie):
    return movie['year']

def get_genre(movie):
    return movie['genre']

def get_rating(movie):
    return movie['rating']

def average_rating(movies):
    ratings = [get_rating(x) for x in movies]
    return sum(ratings) / len(ratings) 

def per_actor(movie, acc):
    for actor in get_actors(movie):
        acc[actor].append(movie)

def per_key(new_key):
    def inner(movie, acc):
        acc[movie[new_key]].append(movie)
    return inner

def pivot(movies, new_key):
    return pivot_ex(movies, per_key(new_key))

def pivot_ex(movies, fn):
    new_dict = defaultdict(list)
    for m in movies:
        fn(m, new_dict)
    return new_dict

