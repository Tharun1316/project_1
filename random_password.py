import random
characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()~?"
password = "".join(random.sample(characters, 16))
print(password)
