import requests
import random

def generate_bin(card_type):
    while True:
        if card_type == "amex":
            bin_number = "37" + str(random.randint(0, 9**4-1)).zfill(4)
        elif card_type == "visa":
            bin_number = "4" + str(random.randint(0, 9**5-1)).zfill(5)
        elif card_type == "mastercard":
            bin_number = "5" + str(random.randint(1, 5)) + str(random.randint(0, 9**3-1)).zfill(3) + str(random.randint(0, 9**2-1)).zfill(2)
        elif card_type == "dinersclub":
            bin_number = random.choice(["300", "301", "302", "303", "304", "305", "36", "38"]) + str(random.randint(0, 9**3-1)).zfill(3) + str(random.randint(0, 9**3-1)).zfill(3)
        elif card_type == "discover":
            bin_number = random.choice(["6011", "65"]) + str(random.randint(0, 9**4-1)).zfill(4) + str(random.randint(0, 9**2-1)).zfill(2)
        elif card_type == "jcb":
            bin_number = "35" + str(random.randint(0, 9**4-1)).zfill(4) + str(random.randint(0, 9**2-1)).zfill(2)
        else:
            print("Invalid card type")
            return None
        
        response = requests.get(f"https://lookup.binlist.net/{bin_number}")
        if response.status_code == 200:
            print(f"Generated BIN: {bin_number}")
            country_name = response.json()['country'].get('name', 'None')
            print(f"Country: {country_name}")
            bank_name = response.json()['bank'].get('name', 'None')
            print(f"Bank: {bank_name}")
            type_name = response.json().get('type', '-')
            print(f"Type: {type_name}")
            brand_name = response.json().get('brand', 'None')
            print(f"Brand: {brand_name}")
            if not response.json().get('prepaid'):
                print("Prepaid: No")
            else:
                print("Prepaid: Yes")
            break

if __name__ == '__main__':
    card_type = input("Type the Credit Card Type: (amex/visa/mastercard/dinersclub/discover/jcb) ")
    generate_bin(card_type.lower())
