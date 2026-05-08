from werkzeug.security import generate_password_hash

hashed_password = generate_password_hash("qwerty")
print(hashed_password)
