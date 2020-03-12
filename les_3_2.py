def user_info(lastname, firstname, email, phone, year_of_birth, city):
    return {"lastname": lastname, "firstname": firstname, "email": email, "phone": phone, "year_of_birth": year_of_birth, "city": city}


user_dict = user_info(email="julia@mail.ru", phone="89521145641", year_of_birth="1991", city="Kaliningrad", lastname="Gribova", firstname="Julia")
print(user_dict)