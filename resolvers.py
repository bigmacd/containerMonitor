
import subprocess


def runCommand(command: str) -> list:
    output = []
    psCommand = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    while True:
        line = psCommand.stdout.readline()
        if line == '' or psCommand.poll() is not None:
            break
        if line:
            output.append(line.decode('utf-8').strip())
    return output

def getRunningContainers():
    command = "/usr/bin/docker ps --format '{{.Names}}:   {{.Status}}'"
    output = runCommand(command)
    retVal = []
    for i in output:
        c, u = i.split(':', 1)
        retVal.append({ "container": c, "status": u})

    return retVal


def getImages():
    imageCommand = "/usr/bin/docker image ls --format '{{.Repository}}!{{.ID}}!{{.Tag}}!{{.CreatedAt}}!{{.Size}}'"
    output = runCommand(imageCommand)
    retVal = []
    for i in output:
        rep, id, tag, created, size = i.split('!')
        retVal.append({ "repository": rep,
                        "imageId": id,
                        "tag": tag,
                        "createdAt": created,
                        "size": size })
    return retVal