# Passwolt's password storage server

Self hosted storage solution for passwolt (if you don't trust any cloud based solution or just want to look cool)

## Get started

This package is the server component for the Passwolt db. Please note: Passwolt db only helps to expose the encrypted
passwords.  It doesn't know about the master password (which is used to encrypt the passwords) and thus cannot
view/modify it anyhow.

### Installation

```
$ pip install passwolt-server
<SNIP>

$ passwolt-server install
...
```

### To run the server

```
$ passwolt-server start
...
```
