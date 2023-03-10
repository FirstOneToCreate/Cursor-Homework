# Create regular class taking 8 params on init - name, last_name, phone_number, address, email, birthday,
# age, sex. Override a printable string representation of Profile class and return:
# list of the params mentioned above

class Profile:
    def __init__(self, name, last_name, phone_number, address, email, birthday, age, sex):
        self.name = name
        self.last_name = last_name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age
        self.sex = sex

    def __str__(self):
        return f"Name: {self.name}\nLast Name: {self.last_name}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nEmail: {self.email}\nBirthday: {self.birthday}\nAge: {self.age}\nSex: {self.sex}"


profile = Profile("Volodymyr", "Volkov", "+380939548891", "Lviv, Ukraine", "v.volko@gmail.com", "10.10.2001", "21", "male")
print(profile)
