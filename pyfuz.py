#Author sidious
import requests
import json
import sys

CYA = '\033[96m'
GRE = '\033[92m'
RED = '\033[31m'
NOR = '\033[0m'

def Banner():
    print(f'''\n{CYA}
    
██████╗ ██╗   ██╗███████╗██╗   ██╗███████╗███████╗███████╗██████╗ 
██╔══██╗╚██╗ ██╔╝██╔════╝██║   ██║╚══███╔╝╚══███╔╝██╔════╝██╔══██╗
██████╔╝ ╚████╔╝ █████╗  ██║   ██║  ███╔╝   ███╔╝ █████╗  ██████╔╝
██╔═══╝   ╚██╔╝  ██╔══╝  ██║   ██║ ███╔╝   ███╔╝  ██╔══╝  ██╔══██╗
██║        ██║   ██║     ╚██████╔╝███████╗███████╗███████╗██║  ██║
╚═╝        ╚═╝   ╚═╝      ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
                            -sidious-                                                              
{NOR}''')

def fuzzer():
    Banner()
    url = input("\n[*] URL to fuzz: ")
    dir_file = input("[*] Fuzz file: ")
    print('-' * 50)
    if len(url) < 1 or len(dir_file) < 1:
        print("Please provide a url and dir file..")
        sys.exit()
    else:
        pass    
    input_file = open(f'{dir_file}', 'r')
    for line in input_file:
        resp = requests.get(f"{url}/{line}")
        if resp.status_code == 404:
            pass
        else:
            try:
                status = resp.status_code
                repheader = resp.headers['content-type']
                result = resp.json()
                hit = line.replace('\n','')
                print(f"\n[*]Hit on:{CYA}",hit)
                print(f"{NOR}[*]Content type:",repheader)
                print(f"{NOR}[*]Status code:{GRE}",status)
                print(f"{NOR}[*]Payload:",result,"\n")
            except json.decoder.JSONDecodeError as err:
                hit = line.replace('\n','')
                repheader = resp.headers['content-type']
                print(f"\n[*]Error on:{RED}",hit)
                print(f"{NOR}[*]Content type:",repheader)
                print(f"{NOR}{err}")
                pass

if __name__ == '__main__':
    try:
        fuzzer()
    except KeyboardInterrupt:   
        print("Exited by user..")
        sys.exit()
    except Exception as err:
        print(f"Could {RED}not{NOR} connect to the API!\nCheck the endpoint url and make sure to use{CYA} http://{NOR}")
    finally:
        print('-' * 50)
        print(' ' * 15, f"{CYA}Fuzzer {NOR}is {GRE}done{NOR}..!\n")
