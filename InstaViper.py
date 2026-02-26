import os
import uuid
import requests
import platform
import time
import random
import string
from colorama import Fore, init
class PasswordReset:
    def __init__(self):
        self.base_url = 'https://i.instagram.com/api/v1/accounts/send_password_reset/'

    def generate_old_user_agent(self):
      
        random_part1 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        random_part2 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        random_part3 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        random_part4 = ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))
        
        user_agent = f'Instagram 150.0.0.0.000 Android (29/10; 300dpi; 720x1440; {random_part1}/{random_part2}; {random_part3}; {random_part4}; en_GB;)'
        return user_agent

    def send_reset(self, data: str):
       
        headers = {
            'user-agent': 'application/x-www-form-urlencoded', 
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        
        try:
            response = requests.post(self.base_url, headers=headers, data=data)
            response_text = response.text
            
            if '"obfuscated_email"' in response_text:
                return True
            else:
                return False
                
        except Exception as e:
            print(f'[{Fore.LIGHTRED_EX}ERROR{Fore.RESET}] Connection error: {str(e)}')
            return False

    def email_reset(self, email: str):
       
        csrf_token = ''.join(random.choices(
            string.ascii_lowercase + string.ascii_uppercase + string.digits, 
            k=32
        ))
        
        data = {
            '_csrftoken': csrf_token,
            'user_email': email,
            'guid': str(uuid.uuid4()),
            'device_id': str(uuid.uuid4())
        }
        
        data_str = '&'.join([f'{k}={v}' for k, v in data.items()])
        return self.send_reset(data_str)

    def username_reset(self, username: str):
        csrf_token = ''.join(random.choices(
            string.ascii_lowercase + string.ascii_uppercase + string.digits, 
            k=32
        ))
        
        data = {
            '_csrftoken': csrf_token,
            'username': username,
            'guid': str(uuid.uuid4()),
            'device_id': str(uuid.uuid4())
        }
        
        data_str = '&'.join([f'{k}={v}' for k, v in data.items()])
        return self.send_reset(data_str)


def display_logo():
    logo = f'''
{Fore.GREEN}
 _ __  _   __ _____ __   _   _  _ ___ ___ ___  
| |  \| |/' _/_   _/  \ | \ / || | _,\ __| _ \ 
| | | ' |`._`. | || /\ |`\ V /'| | v_/ _|| v / 
|_|_|\__||___/ |_||_||_|  \_/  |_|_| |___|_|_\ 
          Made by the Emperor Slay                          
{Fore.RESET}
    '''
    print(logo)


def display_email_logo():
    logo = f'''
{Fore.LIGHTCYAN_EX}                     
 ___ __ __  __  _ _    
| __|  V  |/  \| | |   
| _|| \_/ | /\ | | |_  
|___|_| |_|_||_|_|___| 
                                       
{Fore.RESET} 
    '''
    print(logo)


def display_username_logo():
    logo = f'''
{Fore.BLUE}                                    
 _  _   __  ___ ___ __  _  __  __ __ ___  
| || |/' _/| __| _ \  \| |/  \|  V  | __| 
| \/ |`._`.| _|| v / | ' | /\ | \_/ | _|  
 \__/ |___/|___|_|_\_|\__|_||_|_| |_|___| 
                                                                      
{Fore.RESET}
    '''
    print(logo)


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')


def main():
    reset = PasswordReset()
    
    while True:
        clear_screen()
        display_logo()
        
        options = f'''
>_<>_<>_<>_<>_<>_<>_<>_<>
[{Fore.GREEN}1{Fore.RESET}] - Email Password Reset
[{Fore.GREEN}2{Fore.RESET}] - Username Password Reset
[{Fore.GREEN}3{Fore.RESET}] - Exit
>_<>_<>_<>_<>_<>_<>_<>_<>
        '''
        print(options)
        
        choice = input(f'[{Fore.GREEN}+{Fore.RESET}] Enter your choice idiot: ').strip()
        clear_screen()
        
        if choice == '1':
            display_email_logo()
            email = input(f'[{Fore.GREEN}+{Fore.RESET}] Enter email idiot: ').strip()
            
            if reset.email_reset(email):
                print(f'\n[{Fore.GREEN}+{Fore.RESET}] DONE RESET : {email}')
            else:
                print(f'\n[{Fore.RED}-{Fore.RESET}] ERROR RESET : {email}')

        elif choice == '2':
            display_username_logo()
            username = input(f'[{Fore.GREEN}+{Fore.RESET}] Enter username: ').strip()
            
            if reset.username_reset(username):
                print(f'\n[{Fore.GREEN}+{Fore.RESET}] DONE RESET : {username}')
            else:
                print(f'\n[{Fore.RED}-{Fore.RESET}] ERROR RESET : {username}')
                
        elif choice == '3':
            print(f'\n{Fore.RED}Bye idiot !{Fore.RESET}')
            time.sleep(1)
            break
            
        else:
            print(f'\n{Fore.RED}Invalid choice idiot !{Fore.RESET}')
            time.sleep(2)
            continue
        
        input(f'\n[{Fore.YELLOW}*{Fore.RESET}] Press Enter to continue...')


if __name__ == '__main__':
    main()