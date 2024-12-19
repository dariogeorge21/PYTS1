def celsius_to_farenheit(celsuis):
    farenheit=celsuis*(9/5)+32
    return farenheit
def farenheit_to_celsius(farenheit):
    celsius=(farenheit-32)*(5/9)
    return celsius
print(celsius_to_farenheit(24))