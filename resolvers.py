
import subprocess


def runCommand(command: str) -> list:
    output = []
    psCommand = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    while True:
        line = psCommand.stdout.readline()
        if line:
            output.append(line.decode('utf-8').strip())
        if line == '' or psCommand.poll() is not None:
            break
    return output

def getRunningContainers():
    command = "/usr/local/bin/docker ps --format '{{.Names}}:   {{.Status}}'"
    output = runCommand(command)
    retVal = []
    for i in output:
        c, u = i.split(':', 1)
        retVal.append({ "container": c, "status": u})

    return retVal


def getImages():
    imageCommand = "/usr/local/bin/docker image ls --format '{{.Repository}}!{{.ID}}!{{.Tag}}!{{.CreatedAt}}!{{.Size}}'"
    output = runCommand(imageCommand)
    retVal = []
    for i in output:
        rep, id, tag, created, size = i.split('!')
        retVal.append({ "repository": rep,
                        "imageId": id,
                        "tag": tag,
                        "createdAt": created,
                        "size": size })
    if len(retVal) % 2 != 0:
        retVal.append({ "repository": '',
                        "imageId": '',
                        "tag": '',
                        "createdAt": '',
                        "size": '' })

    return retVal
