import os
import sys
import subprocess
import json

dirname = os.path.dirname(__file__)
usage = '''---
myssh 1.0
Usage: python main.py connect <name>
** name must be defined in {dirname}/hosts.json. **'''.format(dirname=dirname)

f = open(dirname + '/hosts.json', 'r')
jsonData = json.load(f)
f.close()

def main():
    # Fetch a param
    if len(sys.argv) == 1:
        print 'Argument is unspecified.'
        print usage
        sys.exit()
    else:
        connect(sys.argv[1])

def connect(host):
    # Check the existence of the host
    if host in jsonData['ssh-hosts']:
        hostData = jsonData['ssh-hosts'][host]
    else:
        print 'Specified host is not registered in hosts.json.'
        print usage
        sys.exit()

    # Generate a ssh command
    if hostData.has_key('username'):
        command = ['ssh', hostData['username'] + '@' + hostData['address']]
    else:
        command = ['ssh', hostData['address']]
        if hostData.has_key('port'):
            command.append('-p')
            command.append(str(hostData['port']))
        if  hostData.has_key('cert-path'):
            command.append('-i')
            command.append(hostData['cert-path'])

        # Use the ssh command
        print 'Executed command: ' + ' '.join(command)
        subprocess.call(command)
        sys.exit()

if __name__ == '__main__':
    main()
