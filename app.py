import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc

# Lê o arquivo
df = pd.read_csv('ecommerce_estatistica.csv')

# Inicia o app
app = Dash(__name__)
app.title = "Dashboard Ecommerce"

# Layout da aplicação
app.layout = html.Div([
    html.H1("Análise de Dados - E-commerce", style={'textAlign': 'center'}),

    html.H2("Distribuição de Preços"),
    dcc.Graph(
        figure=px.histogram(df, x='Preço', nbins=20, title='Histograma de Preços')
    ),

    html.H2("Dispersão: Nota x Quantidade Vendida"),
    dcc.Graph(
        figure=px.scatter(df, x='Nota', y='Qtd_Vendidos', title='Nota vs Qtd Vendidos')
    ),

    html.H2("Mapa de Calor de Correlação"),
    dcc.Graph(
        figure=px.imshow(df.select_dtypes(include='number').corr(), text_auto=True, title='Correlação entre Variáveis')
    ),

    html.H2("Distribuição por Gênero"),
    dcc.Graph(
        figure=px.pie(df, names='Gênero', title='Distribuição por Gênero', hole=0.3)
    ),

    html.H2("Gráfico de Barras - Quantidade Vendida por Marca"),
    dcc.Graph(
        figure=px.bar(df, x='Marca', y='Qtd_Vendidos', title='Qtd Vendida por Marca')
    ),

    html.H2("Gráfico de Densidade - Preço"),
    dcc.Graph(
        figure=px.density_contour(df, x='Preço', title='Densidade dos Preços')
    )
])

# Roda o servidor
if __name__ == '__main__':
    app.run(debug=True)
