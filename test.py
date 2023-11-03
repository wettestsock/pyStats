import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as spy

x = [2760,6547,6664,4855,4965,5719,7031,5741]
y = [35,22,27,28,24,17,22,21]

pd = pd.DataFrame({'x': [2758,6541,6688,4895,4925,5721,7036,5716],
        'y': [36,22,27,28,24,16,22,21]
})

print(spy.linregress(pd['y'], pd['x']))
sns.regplot(data =pd, x='y', y='x')
plt.show()