import random
import string


def get_userinput():
    while True:
        try:
            p_length = int(input("Provide the length of the password you wish to have (Minimum of 10 characters):  "))
            if p_length <= 10:
                raise ValueError("Password length should be minimim of 10 characters")
            return p_length
        except ValueError as ve:
            print(ve)

def generate_password(p_length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    # To ensure that the password to be complex these are included it, one lower character, one upper character, one number and one punctuation symbol
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice('%(),')
    ]
    
    password += random.choices(all_characters, k=p_length-4)
    random.shuffle(password)
    return ''.join(password)

def main():
    print("... WELCOME TO PASSWORD GENERATOR ...")
    
    # Get user input for the desired password length
    p_length = get_userinput()
    
    # Generate the password
    password = generate_password(p_length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

if __name__ == "__main__":
   main()
