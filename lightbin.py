import http.client
from tabulate import tabulate
from termcolor import colored
import json

def get_bin_info(bin_number):
    conn = http.client.HTTPSConnection("neutrinoapi-bin-lookup.p.rapidapi.com")

    payload = f"bin-number={bin_number}&customer-ip=60.234.81.148"

    headers = {
        'content-type': "application/x-www-form-urlencoded",
        'X-RapidAPI-Key': "87f0b316e0msh4395b1db710fb7ep19b3ddjsnc06bdf0b304b",
        'X-RapidAPI-Host': "neutrinoapi-bin-lookup.p.rapidapi.com"
    }

    conn.request("POST", "/bin-lookup", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")

def format_bin_info(bin_info):
    bin_info_dict = json.loads(bin_info)
    table_data = []
    for key, value in bin_info_dict.items():
        table_data.append([key, value])
    return table_data

def main():
    bin_number = input("Enter the BIN number to get information: ")
    bin_info = get_bin_info(bin_number)
    formatted_info = format_bin_info(bin_info)
    
    headers = ["Attribute", "Value"]
    print(colored(tabulate(formatted_info, headers=headers, tablefmt="fancy_grid"), "cyan"))

if __name__ == "__main__":
    main()
