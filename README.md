# Password Generator

Basic configurable password generator that can create a couple different formats of passwords.

## Configuration options
* Configuration options can be set at the top of Generator.py, right under the imports section

## Module requirements
Only module that doesn't come stock with python (I believe) is `pyperclip`. `Pyperclip` can be installed with:
> pip install pyperclip

## Complexity recommendations

### Products and their maximum password lengths
* Windows 10 - 127 characters
* Windows 10 with MS account - 16 characters
* Yahoo - 32 characters
* Google - 200 characters
* Linux - No limit

## Future Ideas
* Ability to feed it a list of users and have it shoot out a .csv with each username and a distinct random password. (Maybe have it create a batch script and a shell script as well that could make administration super easy)

* Basic installer script files

* Build out a simple API/website

* Password evaluator (fun to do but has already been done to death....)

* GUI version/compiled version/Mobile version

## Open Source inclusions and credit
Dictionary File - https://github.com/dwyl/english-words

### Open Source Python Modules
Pyperclip - https://github.com/asweigart/pyperclip

JSON - https://github.com/simplejson/simplejson

Requests - https://github.com/requests/requests
