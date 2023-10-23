import random
import re
import os
import ctypes
import phonenumbers
from phonenumbers import carrier
from colorama import init, Fore

ctypes.windll.kernel32.SetConsoleTitleW("Jaw @ NL GEN")

def gen(start):
    phone_number = str(start)
    for _ in range(8):
        phone_number += str(random.randint(0, 9))
    return phone_number

def valid_check(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number, "FR")
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def get_number_info(phone_number):
    parsed_number = phonenumbers.parse(phone_number, "FR")
    operator = carrier.name_for_number(parsed_number, "fr")
    return operator

def clean_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)

def sltcv():
    prefixe = "+33"

    isp_num = {}
    generated_numbers = set()

    while True:
        start = random.choice(["6", "7"])
        gen_num = gen(start)

        if valid_check(gen_num) and gen_num not in generated_numbers:
            generated_numbers.add(gen_num)
            numero_isp = get_number_info(gen_num)
            formatted_number = f"{prefixe}{gen_num}"

            if numero_isp:
                isp_num.setdefault(numero_isp, []).append(formatted_number)
                print(f"{Fore.WHITE}GOOD | {formatted_number}{Fore.RESET} | {numero_isp}")
            else:
                print(f"{Fore.RED}BAD {Fore.RED} | {formatted_number}")

            for operator, numeros in isp_num.items():
                operator_filename = clean_filename(f"{operator}.txt")
                with open(operator_filename, "a") as operator_file:
                    for numero in numeros:
                        operator_file.write(numero + '\n')
                isp_num = {}

if __name__ == "__main__":
    sltcv()
