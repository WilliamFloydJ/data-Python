File = open('CupcakeInvoices.csv')
mainTotal_Invoice = 0
chocolate = []
chocolate_total = 0
strawberry = []
strawberry_total = 0
vanilla=[]
vanilla_total = 0
for line in File:
    print(line)
    elements = line.split(',')
    print(elements[2])
    SubTotal_invoice = int(elements[3]) * float(elements[4])
    print(SubTotal_invoice)
    mainTotal_Invoice = round(mainTotal_Invoice + SubTotal_invoice, 2)
    if elements[2] == 'Vanilla':
        vanilla_total = vanilla_total + SubTotal_invoice
        vanilla.append(vanilla_total)
    if elements[2] == 'Chocolate':
        chocolate_total = chocolate_total + SubTotal_invoice
        chocolate.append(chocolate_total)
    if elements[2] == 'Strawberry':
        strawberry_total = strawberry_total + SubTotal_invoice
        strawberry.append(strawberry_total)
print(mainTotal_Invoice)
File.close()

import matplotlib.pyplot as plt

import numpy as np

vanillaPoints = np.array(vanilla)
strawberryPoints = np.array(strawberry)
chocolatePoints = np.array(chocolate)

plt.plot(vanillaPoints)
plt.plot(strawberryPoints)
plt.plot(chocolatePoints)
plt.show()
