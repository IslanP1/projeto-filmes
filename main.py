from flask import Flask, render_template, request, redirect
import tmdbsimple as tmdb

app = Flask(__name__)
tmdb.API_KEY = ""


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return redirect('http://localhost:5000/movie/{}'.format(request.form['title']))
    else:
        return render_template('base.html')


@app.route("/movie/<title>", methods=['GET', 'POST'])
def movie(title):
    results = tmdb.Search().movie(query=title)["results"]

    movie = results[0] if results else None

    poster_url, overview, rating = None, None, None
    if movie:
        movie_id = movie["id"]
        movie_details = tmdb.Movies(movie_id).info(language="pt-BR")

        poster_path = movie["poster_path"]
        poster_url = "https://image.tmdb.org/t/p/w500{}".format(poster_path)

        overview = movie_details["overview"]
        rating = movie_details["vote_average"]
        lancamento = movie_details["release_date"]
        titulo = movie_details["title"]
        popularidade = movie_details["popularity"]
        
        if request.method == 'POST':
            return redirect('http://localhost:5000/')

    return render_template("movie.html", poster_url=poster_url, overview=overview, rating=rating,
                           lancamento=lancamento, titulo=titulo, popularidade=popularidade)


if __name__ == '__main__':
    app.run(debug=True)
