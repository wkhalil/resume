import flask

application = flask.Flask(__name__)


@application.route("/", methods=["GET"])
def home_page():
    return flask.render_template("./index.html")


if __name__ == '__main__':
    application.run(debug=True)