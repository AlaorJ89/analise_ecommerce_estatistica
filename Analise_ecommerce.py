import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Leitura do arquivo


df = pd.read_csv('ecommerce_estatistica.csv', sep=',', quotechar='"', encoding='utf-8')
print(df.head())
print(df.shape)

# Histograma - Distribuição da nota
plt.figure(figsize=(8, 5))
sns.histplot(df['Nota'], bins=10, kde=True)
plt.title('Distribuição das Notas dos Produtos')
plt.xlabel('Nota')
plt.ylabel('Frequência')
plt.show()

# Gráfico de Dispersão - Preço vs Quantidade Vendida
plt.figure(figsize=(8, 5))
sns.scatterplot(x='Preço', y='Qtd_Vendidos', data=df)
plt.title('Relação entre Preço e Quantidade Vendida')
plt.xlabel('Preço')
plt.ylabel('Qtd Vendida')
plt.show()

# Mapa de Calor - Correlação entre variáveis numéricas
plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Mapa de Calor das Correlações')
plt.show()

# Gráfico de Barras - Frequência das Marcas
plt.figure(figsize=(10, 6))
df['Marca'].value_counts().head(10).plot(kind='bar')
plt.title('Top 10 Marcas Mais Frequentes')
plt.xlabel('Marca')
plt.ylabel('Contagem')
plt.show()

# Contagem por gênero
genero_counts = df['Gênero'].value_counts()

#adicionar porcentagem na legenda
labels = [f'{label} ({count/sum(genero_counts)*100:.1f}%)' for label, count in zip(genero_counts.index, genero_counts)]

# Gráfico de pizza sem rótulos
plt.figure(figsize=(8, 8))
plt.pie(genero_counts, labels=None, autopct=None, startangle=140)

# Adiciona legenda fora do gráfico
plt.legend(labels, title="Gênero", loc="best")
plt.title("Distribuição de Gênero")
plt.tight_layout()
plt.show()

# Gráfico de Densidade - Preço
plt.figure(figsize=(8, 5))
sns.kdeplot(df['Preço'], fill=True)
plt.title('Densidade de Preço')
plt.xlabel('Preço')
plt.ylabel('Densidade')
plt.show()

# Gráfico de Regressão - Nota vs Quantidade Vendida
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')
df['Nota'] = pd.to_numeric(df['Nota'], errors='coerce')
plt.figure(figsize=(8, 5))
sns.regplot(x='Nota', y='Qtd_Vendidos', data=df)
plt.title('Relação entre Nota e Quantidade Vendida')
plt.xlabel('Nota')
plt.ylabel('Qtd Vendida')
plt.show()