import pandas as pd

file_path = 'cyberdata.csv'
data = pd.read_csv(file_path)

#Explore data
data.info()
print(data.head())

data['cvss'] = data['cvss'].fillna(0) #Data cleaning

#Data Analysis
import matplotlib.pyplot as plt
import seaborn as sns

##Distribución de Severidad de las Vulnerabilidades:
sns.set(style="whitegrid")
severity_counts = data['severity'].value_counts()

plt.figure(figsize=(10, 6))
severity_counts.plot(kind='bar', color='skyblue')
plt.title('Distribución de Severidad de las Vulnerabilidades')
plt.xlabel('Severidad')
plt.ylabel('Número de Vulnerabilidades')
plt.xticks(rotation=45)
plt.show()

##Distribución de Complejidad de Ataque:
complexity_counts = data['complexity'].value_counts()

plt.figure(figsize=(10, 6))
complexity_counts.plot(kind='bar', color='lightgreen')
plt.title('Distribución de Complejidad de Ataque')
plt.xlabel('Complejidad')
plt.ylabel('Número de Vulnerabilidades')
plt.xticks(rotation=45)
plt.show()

##Distribución de Vectores de Ataque:
vector_counts = data['vector'].value_counts()

plt.figure(figsize=(10, 6))
vector_counts.plot(kind='bar', color='lightcoral')
plt.title('Distribución de Vectores de Ataque')
plt.xlabel('Vector de Ataque')
plt.ylabel('Número de Vulnerabilidades')
plt.xticks(rotation=45)
plt.show()

##Distribución de Puntajes CVSS:
cvss_scores = data['cvss'].dropna()

plt.figure(figsize=(10, 6))
sns.histplot(cvss_scores, bins=10, kde=True, color='lightblue')
plt.title('Distribución de Puntajes CVSS')
plt.xlabel('Puntaje CVSS')
plt.ylabel('Número de Vulnerabilidades')
plt.show()

##Número de Vulnerabilidades por Proveedor y Producto
vendor_counts = data['vendor_project'].value_counts().head(10)
product_counts = data['product'].value_counts().head(10)

plt.figure(figsize=(12, 7))
vendor_counts.plot(kind='bar', color='mediumpurple')
plt.title('Número de Vulnerabilidades por los 10 Principales Proveedores')
plt.xlabel('Proveedor')
plt.ylabel('Número de Vulnerabilidades')
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(12, 7))
product_counts.plot(kind='bar', color='salmon')
plt.title('Número de Vulnerabilidades por los 10 Principales Productos')
plt.xlabel('Producto')
plt.ylabel('Número de Vulnerabilidades')
plt.xticks(rotation=45)
plt.show()

# Dataset ya procesado
data.to_csv('processed_cyberdata.csv', index=False)

# Resumen de proveedores y productos
vendor_counts_df = vendor_counts.reset_index().rename(columns={'index': 'vendor_project', 'vendor_project': 'vulnerability_count'})
product_counts_df = product_counts.reset_index().rename(columns={'index': 'product', 'product': 'vulnerability_count'})

vendor_counts_df.to_csv('vendor_counts.csv', index=False)
product_counts_df.to_csv('product_counts.csv', index=False)