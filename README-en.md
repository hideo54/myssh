# myssh

## About

Sometimes we feel bothersome if we have to change ssh-comand because of managing multiple servers.
By using myssh command, the program loads your ssh settings, so it'll become really easy to ssh.

## Version

Ver 1.0

## Usage

### Setup

#### Download this repository

Hereinafter, [dir-path] means the path where this repository is downloaded.

#### Register host(s) to hosts.json

host.json in this repository includes a sample data.
You should add required host(s) information to it.  
Here are all properties you can describe to the information:

* address **(Required)**  
Specify the address you want to connect. Either IP address and domain can be specified as same as normal ssh command.

* port (Optional)  
Specify the ssh port you want to connect. If it's omitted, the program specifies port-22.

* username (Optional)  
Specify the username you want to use in ssh. If it's omitted, the program specifies the user running myssh command.

* cert-path (Optional)  
Specify the path where the private key is put, if public key authentication is required.

Add the host information mentioned above to ssh-hosts using a name you like.

#### Set an alias of myssh command

Add the following code to ~/.bashrc:
```bash
alias myssh='python [dir-path]/myssh.py $1'
```
Next, execute this:
```bash
source ~/.bashrc
```

### Usage

```
myssh [the host name you specifies in hosts.json]
```

## Contact

* Twitter: [@hideo54](https://twitter.com/hideo54)
* Email: hideo54.pub@gmail.com
