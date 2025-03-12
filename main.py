import random
import string
import re
import streamlit as st


st.markdown(
    """
    <style>
    body, [data-testid="stAppViewContainer"] {
        background: url('https://img.freepik.com/free-vector/gradient-technology-futuristic-background_23-2149122416.jpg?t=st=1741781734~exp=1741785334~hmac=2ba86d26b2bb1ede51b4f8cc019ea5ad3694f7f65ff47d81879bb24913b691e3&w=1060') no-repeat center center fixed;
        background-size: cover;
    }
    .content-box {
        display: flex;
        flex-direction: column;
        justify-content: center;
        width: 900px;
        height: 510px;
        margin-top: 18px;
        position: absolute;
        left: 50%; 
        transform: translateX(-50%);
        border-radius: 14px;
        border: 1px solid #f9f9f9;
        backdrop-filter: blur(30px);
        box-shadow: 0px 4px 4px -1px rgba(0, 0, 0, 0.25);
    }

    h1, p, label{
    color: white !important;
    }
    
    
    .st-emotion-cache-18netey h1 {
        font-size: 50px;
        font-weight: bold;
        text-align: center;
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .st-emotion-cache-1104ytp p {
        font-size: 18px !important;
        text-align: left;
    }
    .stButton>button {
        background-color: #A4B465;
        color: white;
        font-size: 22px !important;
        border-radius: 5px;
        padding: 7px;
        width: 100%;
        border: none;
        margin-top: 10px;
        transition: transform 0.4s ease-in-out;
    }
    .stButton>button:hover, 
    .stButton>button:focus, 
    .stButton>button:active, 
    .stButton>button:visited {
        background-color: #626F47;
        transform: scale(1.03);
    }
    .st-ay {
        font-size: 1.6rem;
    }
    .st-bc {
        color: white !important;
    }
    .stRadio [role="radiogroup"] label {
        color: white !important;
        font-size: 20px !important;
        
    }
    .st-emotion-cache-1hyd1ho p {
        font-size: 18px !important;
    }
    .st-ay {
        font-size: 1.1rem;
    }
    .stSlider .st-emotion-cache-1fx8m56 {
        color: white !important;
    }
    .stSlider .st-emotion-cache-10trblm {
        background: white !important;
        border-radius: 10px;
    }
    .stSlider .st-emotion-cache-1wy0on6 {
        background: blue !important;
    }
    @media (max-width: 768px) {
        .content-box {
            width: 105%;
            min-height: auto;
            padding: 10px;
            
        }
        h1 {
            font-size: 22px !important;
            text-align: center;
        }
        .stButton>button {
            font-size: 16px !important;
            padding: 8px;
        }
        .st-ay {
            font-size: 0.8rem;
        }
        .st-emotion-cache-1104ytp p {
            font-size: 16px !important;
            text-align: center;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

def generate_password(length=8):
    if length < 8:
        return "Password must be at least 8 characters long!"
    
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation
    all_chars = lower + upper + digits + symbols
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]
    
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    
    return "".join(password)

def check_password_strength(password):
    strength_criteria = 0
    
    if len(password) >= 8:
        strength_criteria += 1
    if re.search(r'[A-Z]', password):
        strength_criteria += 1
    if re.search(r'[a-z]', password):
        strength_criteria += 1
    if re.search(r'\d', password):
        strength_criteria += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_criteria += 1
    
    if strength_criteria <= 2:
        return "Weak Password 😓"
    elif strength_criteria in [3, 4]:
        return "Medium Strength Password 😊"
    else:
        return "Strong Password 💪"

st.markdown('<div class="content-box">', unsafe_allow_html=True)
st.markdown('<h1 class="title">🔐 Password Generator & Strength Checker</h1>', unsafe_allow_html=True)
st.markdown('<p class="description">Generate or enter password to check its strength.</p>', unsafe_allow_html=True)

option = st.radio("Choose an option:", ("Generate Password", "Check Password Strength"))

if option == "Generate Password":
    length = st.slider("Select Password Length:", min_value=8, max_value=32, value=12)
    if st.button("Generate Password"):
        password = generate_password(length)
        st.success(f"Generated Password: `{password}`")

elif option == "Check Password Strength":
    password = st.text_input("Enter your password:", type="password")
    if st.button("Check Strength"):
        strength = check_password_strength(password)
        st.info(f"Password Strength: {strength}")
