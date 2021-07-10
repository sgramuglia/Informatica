import pandas as pd #Pandas para usar dataframes
import matplotlib.pyplot as plt #Para graficar
import matplotlib.cm as cm #Para graficar el silhouette
import seaborn as sns #Para graficar
import numpy as np #Para realizar operaciones númericas con matrices y arrays
from sklearn import datasets #sklearn es LA biblioteca de machine learning de python
from sklearn.cluster import KMeans, DBSCAN #Para usar kmeans
from sklearn.preprocessing import StandardScaler #Para estandarizar nuestros datos
from sklearn.metrics import silhouette_samples, silhouette_score #Para el coeficiente de silhouette
from sklearn.cluster import AgglomerativeClustering #Para clustering jerárquico
from sklearn.metrics import pairwise_distances #Para las distancias a pares
from scipy.cluster.hierarchy import dendrogram, cophenet, linkage #Para graficar los dendrogramas y calcular el coeficiente cofenetico
from scipy.cluster import hierarchy #Para graficar los dendrogramas
from scipy.spatial.distance import pdist #Para calcular la distancia con el coeficiente cofenetico
import community as community_louvain #Para louvain
import networkx as nx #Para grafos


stock_data = pd.read_csv("C:\Info\dataset_clustering_teorico.csv")
stock_data.head()
stock_data.info()
stock_data.describe()

descripcion_por_empresa = pd.DataFrame()
descripcion_por_empresa["Empresas"] = stock_data["Unnamed: 0"]
descripcion_por_empresa["Media"] = stock_data.mean(axis=1)
descripcion_por_empresa["Mediana"] = stock_data.median(axis=1)
descripcion_por_empresa["Mínimo"] = stock_data.min(axis=1)
descripcion_por_empresa["Máximo"] = stock_data.max(axis=1)
descripcion_por_empresa

g = sns.pairplot(descripcion_por_empresa)

g_medias = sns.histplot(data = descripcion_por_empresa, x = "Media", binwidth=0.25, kde = True)
g_medianas = sns.histplot(data = descripcion_por_empresa, x = "Mediana", binwidth=0.25, kde = True)
g_max = sns.histplot(data = descripcion_por_empresa, x = "Máximo", binwidth=0.25, kde = True)
g_min = sns.histplot(data = descripcion_por_empresa, x = "Mínimo", binwidth=0.25, kde = True)

dxe_solo_float=pd.DataFrame()
dxe_solo_float["Media"]=descripcion_por_empresa["Media"]
dxe_solo_float["Mediana"]=descripcion_por_empresa["Mediana"]
dxe_solo_float["Mínimo"]=descripcion_por_empresa["Mínimo"]
dxe_solo_float["Máximo"]=descripcion_por_empresa["Máximo"]
dxe_solo_float

scaler = StandardScaler()
dxe_escaleado=scaler.fit_transform(dxe_solo_float)

# K = 2
kmeans2 = KMeans(n_clusters = 2, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans2.fit(dxe_escaleado)
colores2 = ["red", "green"]
g_grupos2 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans2.labels_, palette = colores2, alpha = 0.5)
g_centroides2 = sns.scatterplot(x = kmeans2.cluster_centers_[:,2], y = kmeans2.cluster_centers_[:,3], zorder = 10, palette = colores2, hue = [0, 1], legend = False, marker=6, s=200)

# K = 3
kmeans3 = KMeans(n_clusters = 3, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans3.fit(dxe_escaleado)
colores3 = ["red", "green", "blue"]
g_grupos3 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans3.labels_, palette = colores3, alpha = 0.5)
g_centroides3 = sns.scatterplot(x = kmeans3.cluster_centers_[:,2], y = kmeans3.cluster_centers_[:,3], zorder = 10, palette = colores3, hue = [0, 1, 2], legend = False, marker=6, s=200)

# K = 4
kmeans4 = KMeans(n_clusters = 4, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans4.fit(dxe_escaleado)
colores4 = ["red", "green", "blue", "yellow"]
g_grupos4 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans4.labels_, palette = colores4, alpha = 0.5)
g_centroides4 = sns.scatterplot(x = kmeans4.cluster_centers_[:,2], y = kmeans4.cluster_centers_[:,3], zorder = 10, palette = colores4, hue = [0, 1, 2, 3], legend = False, marker=6, s=200)

# K = 5
kmeans5= KMeans(n_clusters =5, init="random", n_init=10, max_iter=300, random_state=123457)
kmeans5.fit(dxe_escaleado)
colores5 = ["red", "green", "blue", "yellow", "violet"]
g_grupos5 = sns.scatterplot(x = dxe_escaleado[:,2], y = dxe_escaleado[:,3], hue = kmeans5.labels_, palette = colores5, alpha = 0.5)
g_centroides5 = sns.scatterplot(x = kmeans5.cluster_centers_[:,2], y = kmeans5.cluster_centers_[:,3], zorder = 10, palette = colores5, hue = [0, 1, 2, 3, 4], legend = False, marker=6, s=200)

inertias_dict = {}
inertias_dict["K"] = []
inertias_dict["Inertia"] = []

for i in range(15):
  k = i + 1
  kmeans_ = KMeans(n_clusters = k, init="random", n_init=10, max_iter=300, random_state=123457)
  kmeans_.fit(dxe_escaleado)
  inertias_dict["K"].append(k)
  inertias_dict["Inertia"].append(kmeans_.inertia_)
print(inertias_dict)

inertias_df = pd.DataFrame(inertias_dict)
inertias_df

sns.pointplot(data=inertias_df,x = "K",y = "Inertia")


stock_data_solo_float=stock_data.drop(["Unnamed: 0"],axis=1)
scaler=StandardScaler()
stock_data_normalizado = scaler.fit_transform(stock_data_solo_float)


kmeans14 = KMeans(n_clusters = 14, init  ="random", n_init = 10, max_iter=300, random_state=123457)
kmeans14.fit(stock_data_normalizado)

#Para más colores: https://matplotlib.org/stable/gallery/color/named_colors.html
import matplotlib.colors as mcolors
colores14 = ["darkgray","lightcoral","firebrick","orangered","peru","lightgreen","yellow","bisque","green","turquoise","darkslategray","purple","deeppink","cadetblue"]
g_grupos14 = sns.scatterplot(x = stock_data_normalizado[:,2], y = stock_data_normalizado[:,3], hue = kmeans14.labels_, palette = colores14, alpha = 0.5)
g_centroides14 = sns.scatterplot(x = kmeans14.cluster_centers_[:,2], y = kmeans14.cluster_centers_[:,3], zorder = 10, palette = colores14, hue = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], legend = False, marker=6, s=200)
