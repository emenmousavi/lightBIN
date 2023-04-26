# lightBIN
LightBIN is a Python program that generates live and working BIN (Bank Identification Number) numbers for credit cards. The program can generate BIN numbers from all countries in the world, and allows the user to choose from the following credit card types:
- American Express (amex)
- Visa
- Mastercard
- Diners Club
- Discover
- JCB

## Installation
To use LightBIN, first make sure you have Python 3.6 or higher installed. Then, you can install the necessary dependencies by running:
```
pip install -r requirements.txt
```

## Usage
To generate a BIN number, run the following command:
```python
python lightbin.py
```

The program will prompt you to enter the type of credit card you want to generate a BIN for. Once you have entered a valid card type, the program will generate a BIN number and check it against the binlist.net database to ensure that it is live and working. If the BIN is valid, the program will print out the BIN number, the country associated with the BIN, the bank that issued the card, the card type, and whether or not the card is a prepaid card.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/emenmousavi/lightBIN/blob/main/LICENSE) file for details.
