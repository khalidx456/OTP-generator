import random
def generate_otp():
    otp = random.randint(1000, 9999)
    return otp
# Example usage
otp = generate_otp()
print("Your OTP:", otp)