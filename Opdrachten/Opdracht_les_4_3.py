phone_numbers = {"The Simpsons": "636-555-3226",
                 "Vegas Vacation": "555-0100",
                 "Ghostbusters": "555-23678",
                 "Billy Madison": "555-0840",
                 "Swingers": "213-555-4679",
                 "Bruce Almighty": "555-0123",
                 "Seinfeld": "555-FILK",
                 "Arrested Development": "555-0113",
                 "Die Hard With a Vengeance": "555-0001",
                 "The A-Team": "555-6162"}


print(f"Het telefoonnummer van Bruce Almighty is {phone_numbers['Bruce Almighty']}")


phone_numbers["Harry Potter"] = "605-475-6961"


oude_nummer = phone_numbers["Ghostbusters"]
phone_numbers["Ghostbusters"] = "555-2368"
print(f"Het telefoonnummer {oude_nummer} van de Ghostbusters is gewijzigd naar {phone_numbers['Ghostbusters']}.")


verwijderd_nummer = phone_numbers.pop("Seinfeld")
print(f"Telefoonnummer {verwijderd_nummer} van Seinfeld is verwijderd.")


aantal_telefoonnummers = len(phone_numbers)
print(f"In de dictionary zitten {aantal_telefoonnummers} telefoonnummers.")
