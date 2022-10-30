# Pyfuz
This is a simple API fuzzer written in python. There is an example FastApi and wordlist included to test with.

## Usage
```bash
#Clone this repository:
$ git clone https://github.com/insidious-security/pyfuz.git

#*Optional; Install the requirements when using the included API:
$ pip3 install -r requirements.txt

#Start the api:
$ uvicorn --reload fapi:app --host 0.0.0.0

#Test the fuzzer:
$ python pyfuz.py

[sidious@deathstar pyfuz]$ python pyfuz.py 


    
██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ █████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║        ██║   ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                            -sidious-                                                              


[*] URL to fuzz: http://example.api:8000
[*] Fuzz file: small.txt

```

The Fuzzer shows both hits on successful urls and errors when encountered.

```
[*]Hit on: blackarch
[*]Content type: application/json
[*]Status code: 200
[*]Payload: [{'User': 'a', 'date': '2022-10-30', 'count': 1}, {'User': 'b', 'date': '2022-10-30', 'count': 2}] 


[*]Error on: docs
[*]Content type: text/html; charset=utf-8
Expecting value: line 2 column 5 (char 5)
```
