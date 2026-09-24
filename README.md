# 🔐 Secure Password Generator

A Python-based secure password generator that creates random passwords using uppercase letters, lowercase letters, numbers, and special symbols.

## ✨ Features

- Generate secure random passwords
- Choose password length
- Include uppercase and lowercase letters
- Include numbers and special symbols
- Evaluate password strength
- Generate multiple passwords
- Input validation

## 🛠️ Technologies Used

- Python
- `secrets` module
- `string` module

## 🚀 How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Run:

```bash
python pass_generator.py
```
## 💻 How It Works

The program first asks the user to enter the required password length.

Then, the user can choose which character types should be included:

- Uppercase letters
- Lowercase letters
- Digits
- Special symbols

The program ensures that at least one character from each selected category is included in the generated password.

The remaining characters are randomly selected from the combined character pool.

Finally, the characters are securely shuffled and the password strength is evaluated.

## 🔒 Security

This project uses Python's `secrets` module instead of the standard `random` module.

The `secrets` module is designed for generating random values suitable for security-sensitive applications such as passwords and authentication tokens.

> **Note:** This project is intended for learning and portfolio purposes. For highly sensitive accounts, consider using a trusted password manager.

## 📊 Password Strength

The password strength is calculated based on:

- Password length
- Lowercase letters
- Uppercase letters
- Numbers
- Special characters

The program displays one of three strength levels:

| Strength | Description |
|----------|-------------|
| Weak | Low variety and/or short length |
| Moderate | Reasonable combination of characters |
| Strong | Good length and character variety |

## 🖥️ Example

```text
=============================================
      SECURE PASSWORD GENERATOR
=============================================

Enter password length (minimum 4, recommended 12+): 12

Select character types to include:
Include uppercase letters (A-Z)? [Y/n]: y
Include lowercase letters (a-z)? [Y/n]: y
Include digits (0-9)? [Y/n]: y
Include special symbols (!@#$...)? [Y/n]: y

---------------------------------------------
Generated Password: X7@mK2!qP9#z
Strength Level:     Strong
---------------------------------------------
```
Generate another password? [y/N]: n

Goodbye!
