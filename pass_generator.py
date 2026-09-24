import secrets
import string


def get_yes_no(prompt, default="y"):
    """Helper to validate yes/no user input."""
    valid_responses = {"y": True, "yes": True, "n": False, "no": False}
    prompt_suffix = " [Y/n]: " if default == "y" else " [y/N]: "
    
    while True:
        choice = input(prompt + prompt_suffix).strip().lower()
        if not choice:
            return valid_responses[default]
        if choice in valid_responses:
            return valid_responses[choice]
        print("[!] Please enter 'y' for yes or 'n' for no.")


def get_password_length():
    """Prompt user for a valid password length."""
    while True:
        user_input = input("Enter password length (minimum 4, recommended 12+): ").strip()
        try:
            length = int(user_input)
            if length < 4:
                print("[!] Length must be at least 4 to allow diverse character types.")
                continue
            return length
        except ValueError:
            print("[!] Please enter a valid positive integer.")


def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    """
    Generates a cryptographically secure random password.
    Guarantees at least one character from each selected character set.
    """
    char_pools = []
    guaranteed_chars = []

    if use_upper:
        char_pools.append(string.ascii_uppercase)
        guaranteed_chars.append(secrets.choice(string.ascii_uppercase))
    if use_lower:
        char_pools.append(string.ascii_lowercase)
        guaranteed_chars.append(secrets.choice(string.ascii_lowercase))
    if use_digits:
        char_pools.append(string.digits)
        guaranteed_chars.append(secrets.choice(string.digits))
    if use_symbols:
        # Common safe symbols (excluding problematic characters like space/quotes if needed)
        symbols = "!@#$%^&*()-_=+[]{}|;:,.<>?"
        char_pools.append(symbols)
        guaranteed_chars.append(secrets.choice(symbols))

    if not char_pools:
        raise ValueError("At least one character set must be selected.")

    if length < len(guaranteed_chars):
        raise ValueError(
            f"Length must be at least {len(guaranteed_chars)} to satisfy selected options."
        )

    # Combine all allowed characters
    combined_pool = "".join(char_pools)

    # Fill the remaining length with random choices from the entire pool
    remaining_length = length - len(guaranteed_chars)
    random_fill = [secrets.choice(combined_pool) for _ in range(remaining_length)]

    # Merge guaranteed characters with the fill
    password_chars = guaranteed_chars + random_fill

    # Cryptographically secure in-place shuffle
    shuffled_chars = []
    while password_chars:
        index = secrets.randbelow(len(password_chars))
        shuffled_chars.append(password_chars.pop(index))

    return "".join(shuffled_chars)


def evaluate_strength(password):
    """Calculates a quick strength rating based on variety and length."""
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1

    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(c in string.punctuation for c in password)

    score += sum([has_lower, has_upper, has_digit, has_symbol])

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Moderate"
    else:
        return "Strong"


def main():
    print("=" * 45)
    print("      SECURE PASSWORD GENERATOR      ")
    print("=" * 45)

    while True:
        length = get_password_length()

        print("\nSelect character types to include:")
        use_upper = get_yes_no("Include uppercase letters (A-Z)?")
        use_lower = get_yes_no("Include lowercase letters (a-z)?")
        use_digits = get_yes_no("Include digits (0-9)?")
        use_symbols = get_yes_no("Include special symbols (!@#$...)?")

        if not any([use_upper, use_lower, use_digits, use_symbols]):
            print("\n[!] Error: You must enable at least one character type!\n")
            continue

        try:
            password = generate_password(
                length, use_upper, use_lower, use_digits, use_symbols
            )
            strength = evaluate_strength(password)

            print("\n" + "-" * 45)
            print(f"Generated Password: {password}")
            print(f"Strength Level:     {strength}")
            print("-" * 45)

        except ValueError as err:
            print(f"\n[!] Generation failed: {err}")

        # Ask to generate another
        if not get_yes_no("\nGenerate another password?", default="n"):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()