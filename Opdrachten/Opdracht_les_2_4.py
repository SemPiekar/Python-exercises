from math import pow

t = 4
v = 179875474.8
c = 299792458

delta = t * 1 / (v * (1 - pow(v, 2) / pow(c, 2)))

print(f'Vanaf een komeet gezien zit u {delta} uur op de tuinstoel'  )
print(f'Vanaf een komeet gezien zit u {delta * 60} minuten op de tuinstoel'  )
print(f'Vanaf een komeet gezien zit u {delta * 3600} seconden op de tuinstoel'  )
