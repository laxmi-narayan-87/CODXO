import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_symbols=True, exclude_ambiguous=True):
    """
    Generates a random password with the given length and criteria.
    The password can include uppercase, lowercase, digits, and symbols.
    Ambiguous characters can be excluded.
    """
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_digits else ""
    symbols = string.punctuation if include_symbols else ""
    
    if exclude_ambiguous:
        ambiguous = 'il1Lo0O'
        lower = ''.join(ch for ch in lower if ch not in ambiguous)
        upper = ''.join(ch for ch in upper if ch not in ambiguous)
        digits = ''.join(ch for ch in digits if ch not in ambiguous)
        symbols = ''.join(ch for ch in symbols if ch not in ambiguous)
        
    all_characters = lower + upper + digits + symbols
    
    if not all_characters:
        raise ValueError("No characters available to generate password.")
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    length = int(input("Enter the length of the password: "))
    include_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    include_digits = input("Include digits? (y/n): ").lower() == 'y'
    include_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    exclude_ambiguous = input("Exclude ambiguous characters? (y/n): ").lower() == 'y'
    
    try:
        password = generate_password(length, include_uppercase, include_digits, include_symbols, exclude_ambiguous)
        print(f"Generated Password: {password}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
