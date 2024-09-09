choice = input("Welke verbinding wilt U gebruiken [4g, 5g, Wifi open] : ").lower()
if choice == "4g":
    print(f'U bent verbonden met 4G!')
elif choice == "5g":
    print(f'U bent verbonden met 5G!')
elif choice == "wifi open":
    print(f'U bent verbonden met Wifi open!')
else:
    print(f'Onbekende invoer, er wordt geen verbinding tot stand gebracht.')
