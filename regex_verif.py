import re

def username(text):
    return re.match(r"^[a-zA-Z0-9_.-]{3,30}$", text)

def email(text):
    return re.match(r"[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+", text)

def passworld(text):
    return re.match(r"^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$", text)