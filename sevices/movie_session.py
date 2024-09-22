from db.models import MovieSession, CinemaHall, Movie
from django.shortcuts import get_object_or_404


def create_movie_session(
        movie_show_time: str,
        movie_id: int,
        cinema_hall_id: int) -> None:
    MovieSession.objects.create(
        show_time=movie_show_time,
        cinema_hall=CinemaHall.objects.get(id=cinema_hall_id),
        movie=Movie.objects.get(id=movie_id)
    )


def get_movies_sessions(session_date: str = None) -> MovieSession:
    if session_date:
        return MovieSession.objects.filter(show_time__date=session_date)
    return MovieSession.objects.all()


def get_movie_session_by_id(movie_session_id: int) -> MovieSession:
    return MovieSession.objects.get(id=movie_session_id)


def update_movie_session(
        session_id: int,
        show_time: str = None,
        movie_id: int = None,
        cinema_hall_id: int = None
) -> MovieSession:
    movie_session = get_object_or_404(MovieSession, id=session_id)

    if show_time:
        movie_session.show_time = show_time

    if movie_id:
        movie = get_object_or_404(Movie, id=movie_id)
        movie_session.movie = movie

    if cinema_hall_id:
        cinema_hall = get_object_or_404(CinemaHall, id=cinema_hall_id)
        movie_session.cinema_hall = cinema_hall

    movie_session.save()

    return movie_session


def delete_movie_session_by_id(session_id: int) -> None:
    movie_session = get_object_or_404(MovieSession, id=session_id)
    movie_session.delete()