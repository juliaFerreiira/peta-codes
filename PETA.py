import math
import pandas as pd
import matplotlib.pyplot as plt
from IPython.display import display

#Data to estimate population growth and flow
print('-'*45)
print('Estimate population growth')
print('-'*45)

t0 = float(input('Starting year: '))
t1 = int(input('Final year: '))
P0 = int(input('Initial population: '))
P1 = int(input('Final population: '))
ec = int(input('Estimate population growth: '))
qpc = float(input('Per capita consumption (L/s): '))
qeta = float(input('Water consumption at ETA (%): '))
Qs = float(input('Singular flow of the large consumer (L/s): '))
h = int(input('Operating period (h): '))
print('-'*45)

#Estimate
Ka = ((P1-P0)/(t1-t0))
Kg = ((math.log(P1) - math.log(P0))/ (t1 -t0))
k1 = 1.2   #Value Tabulated
k2 = 1.5   #Value Tabulated

#Formulas + Loop
data = []
for t in range(t1 + 1, ec + 1):
    Pa = (P0 + (Ka * (t - t0)))
    Pg = P0 * math.exp(Kg * (t - t0))
    qmed = ((Pg * qpc)/ 86400)
    qprod = ((qmed * k1 * 24)/h) * (1 + (qeta/100)) + Qs
    qaat = ((qmed * k1 * 24)/h) + Qs
    qdist = (qmed * k1 * k2) + Qs
    data.append([t, Pa, Pg, qmed, qprod, qaat, qdist])

#Table
df = pd.DataFrame(data, columns= ['Growth Estimate', 'Arithm.Prog', 'Geom.Prog', 'Qméd', 'Qprod', 'Qaat', 'Qdist'])

stylized_table = (
    df.style
    .format({
        'Arithm.Prog': '{:.0f}',
        'Geom.Prog': '{:.0f}',
        'Qméd': '{:.2f}',
        'Qprod': '{:.2f}',
        'Qaat': '{:.2f}',
        'Qdist': '{:.2f}'
    })
    .set_table_styles([
        {'selector': 'th', 'props': [
            ('background-color', '#1B4F72'),
            ('color', 'white'),
            ('font-weight', 'bold'),
            ('text-align', 'center')
        ]},
        {'selector': 'td', 'props': [
            ('text-align', 'center')
        ]}
    ])
)
display(stylized_table)

#Graphic
plt.figure()   #Graph block
plt.plot(df['Growth Estimate'], df['Arithm.Prog']) #Graph lines - comparison
plt.plot(df['Growth Estimate'], df['Geom.Prog'])  #Graph lines - comparison

plt.xlabel('Year')
plt.ylabel('Population')
plt.title('Estimate population growth')

plt.show()