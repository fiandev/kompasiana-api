from application.core import app
from application.controllers.WelcomeController import WelcomeController
from application.controllers.api.ProfileController import ProfileController
from application.controllers.api.PostController import PostController

# web route example
@app.route("/")
def Home ():
    return WelcomeController.index()

# api route example
@app.route("/api/profile/<username>")
def profile (username):
    return ProfileController.index(username=username)

@app.route("/api/post/<username>/<prefix>/<slug>")
def post (username, prefix, slug):
    return PostController.show(username=username, prefix=prefix, slug=slug)