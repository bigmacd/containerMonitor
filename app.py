import subprocess
from flask import Flask, render_template
import pdb

app = Flask(__name__)


def getRunningContainers():
    output = []
    psCommand = subprocess.Popen("/usr/bin/docker ps --format '{{.Names}}:   {{.Status}}'", shell=True, stdout=subprocess.PIPE)
    while True:
        line = psCommand.stdout.readline()
        if line == '' or psCommand.poll() is not None:
            break
        if line:
            output.append(line.decode('utf-8').strip())
    retVal = {}
    for i in output:
        c, u = i.split(':')
        retVal[c] = u
    return retVal


@app.route('/')
def hello():
    return render_template("show_containers.html", entries=getRunningContainers())


if __name__ == '__main__':
    app.run()



