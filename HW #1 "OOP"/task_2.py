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
        return "\n".join([f"Name: {self.name}",
                          f"Last Name: {self.last_name}",
                          f"Phone Number: {self.phone_number}",
                          f"Address: {self.address}",
                          f"Email: {self.email}",
                          f"Birthday: {self.birthday}",
                          f"Age: {self.age}",
                          f"Sex: {self.sex}"])


profile = Profile("Volodymyr", "Volkov", "+380939548891", "Lviv, Ukraine", "v.volko@gmail.com", "10.10.2001", "21",
                  "male")
print(profile)
