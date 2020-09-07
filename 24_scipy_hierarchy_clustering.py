import pandas as  pd
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt

df = pd.read_csv('countries_postions.csv')
print(df.head(10))

longtitude_latitude = df.iloc[:,1:]
linked = linkage(longtitude_latitude, 'ward')


labels = list(df['country'])
print(labels)

dendrogram(linked, orientation='right',labels=labels)
plt.tight_layout()
plt.show()