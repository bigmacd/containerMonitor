import argparse
from flask import Flask, render_template
import pdb
from resolvers import getRunningContainers, getImages

app = Flask(__name__)
noDocker = False


@app.route('/containers')
def hello():
    containers = getRunningContainers()
    return render_template("containers.html", containers = containers, len = len(containers))

@app.route('/images')
def images():
    images = getImages()
    return render_template("images.html", images = images, len = len(images))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--noDocker", action='store_true', help="test without having Docker")
    args = parser.parse_args()

    # if no command line parameter was specified, default to True
    if args.noDocker:
        noDocker = True

    app.run()



