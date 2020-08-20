import argparse 
from flask import Flask, render_template
import pdb
from resolvers import getRunningContainers, getImages

app = Flask(__name__)
noDocker = False


@app.route('/')
def hello():
    images = getImages()
    containers = getRunningContainers()
    return render_template("main.html", images = images, containers = containers)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--noDocker", action='store_true', help="test without having Docker")
    args = parser.parse_args()

    # if no command line parameter was specified, default to True
    if args.noDocker:
        noDocker = True

    app.run()



