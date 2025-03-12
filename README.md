# Password Generator & Strength Checker

## Overview
This is a Streamlit-based web application that allows users to generate secure passwords and check the strength of their existing passwords. The interface features a visually appealing background, and the UI elements are styled for a better user experience.

## Features
- Generate strong passwords of customizable length (minimum 8 characters).
- Ensure at least one lowercase letter, one uppercase letter, one digit, and one special character in generated passwords.
- Evaluate password strength based on complexity rules.
- User-friendly interface with a modern, responsive design.

## Technologies Used
- **Python** for backend logic
- **Streamlit** for web application development
- **Random & String Modules** for password generation
- **Regex (re module)** for password strength validation
- **Custom CSS** for styling UI components

## Installation & Setup
1. Clone the repository or download the script.
2. Install the required dependencies using pip:
   ```sh
   pip install streamlit
   ```
3. Run the application:
   ```sh
   streamlit run script.py
   ```

## Usage
1. Open the application in a browser after running the Streamlit command.
2. Select one of the following options:
   - **Generate Password**: Choose a password length and generate a secure password.
   - **Check Password Strength**: Enter an existing password to assess its strength.
3. View the generated password or strength rating displayed on the screen.

## Customization
- Modify the **background image** in the CSS section to change the theme.
- Adjust the **password length constraints** in the function `generate_password()`.
- Modify password strength criteria in `check_password_strength()` to apply custom rules.

## Contributions
Feel free to submit pull requests or suggest improvements to enhance functionality or design!

