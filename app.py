import subprocess
import argparse 
from flask import Flask, render_template
import pdb

app = Flask(__name__)
noDocker = False

def getRunningContainers():
    output = []
    psCommand = subprocess.Popen("/usr/bin/docker ps --format '{{.Names}}:   {{.Status}}'", shell=True, stdout=subprocess.PIPE)
    while True:
        line = psCommand.stdout.readline()
        if line == '' or psCommand.poll() is not None:
            break
        if line:
            output.append(line.decode('utf-8').strip())
    retVal = []
    for i in output:
        c, u = i.split(':')
        retVal.append({ "container": c, "status": u})
    
    if noDocker:
        return [ { "container": "adminapi", "status": "up" }, { "container":"netezzaapi", "status":"exited"}]
    else:
        return retVal


@app.route('/')
def hello():
    return render_template("show_containers.html", entries=getRunningContainers())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--noDocker", action='store_true', help="test without having Docker")
    args = parser.parse_args()

    # if no command line parameter was specified, default to True
    if args.noDocker:
        noDocker = True

    app.run()



