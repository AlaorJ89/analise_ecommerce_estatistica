# Análise de Dados de E-commerce

Este projeto explora e visualiza dados de um e-commerce a partir do arquivo **`ecommerce_estatistica.csv`**. O objetivo é extrair padrões e gerar insights úteis para decisões de negócio (por exemplo: quais atributos influenciam mais as vendas, distribuição de preços, perfis de público e correlações entre variáveis).

---

## Estrutura do repositório

```text
.
├── Analise_ecommerce.py         # Script principal: leitura do CSV + geração dos gráficos
├── ecommerce_estatistica.csv   # Conjunto de dados (495 linhas × 24 colunas)
└── README.md                   # Este arquivo
Visualizações geradas
Gráfico	Propósito
Histograma	Distribuição dos preços dos produtos
Gráfico de dispersão	Relação entre preço × vendas e nota × vendas
Mapa de calor	Correlação entre todas as variáveis numéricas
Gráfico de barras	Top N marcas (ou materiais) mais frequentes
Gráfico de pizza	Proporção de produtos por gênero
Gráfico de densidade	Distribuição suave dos preços
Gráfico de regressão	Tendência entre nota média e quantidade vendida

Tecnologias
Python 3.11+

Pandas

Matplotlib

Seaborn

Como executar
Clone o repositório:

bash
Copy
Edit
gh repo clone AlaorJ89/analise_ecommerce_estatistica
cd analise_ecommerce_estatistica
(Opcional) Crie e ative um ambiente virtual:

bash
Copy
Edit
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
Instale as dependências:

bash
Copy
Edit
pip install pandas matplotlib seaborn
Execute o script:

bash
Copy
Edit
python Analise_ecommerce.py
Os gráficos serão exibidos em janelas interativas. Feche cada uma para continuar a execução.

Principais insights (exemplo)
Preço vs. Vendas: produtos com faixa de preço intermediária apresentaram maior volume de vendas.

Correlação forte entre número de avaliações e quantidade vendida.

Gênero predominante (ex.: Masculino) representa cerca de 70% do portfólio — possível oportunidade de expansão.

Outliers em vendas indicam possíveis promoções ou inconsistências nos dados.

(Substitua pelos seus próprios comentários após analisar os resultados.)

# Aplicação Interativa com Dash 
Nesta etapa do projeto, criei uma aplicação interativa utilizando a biblioteca Dash. O objetivo é permitir que qualquer usuário visualize os principais gráficos e insights da análise sem precisar executar código Python.

A aplicação inclui:

Visualização de histogramas, gráficos de dispersão, pizza, barras, regressão e densidade

Mapa de calor com correlação entre variáveis

Interface com fundo personalizado via CSS

Para rodar localmente:

bash
Copy
Edit
pip install dash plotly pandas
python app.py
O aplicativo será iniciado no navegador padrão, normalmente em http://127.0.0.1:8050/.

Contribuição
Contribuições são bem-vindas! Abra uma issue ou envie um pull request com melhorias ou novas análises.

Contato
Dúvidas ou sugestões? Entre em contato pelo e-mail alrsj89@gmail.com ou via https://www.linkedin.com/in/alaor-jorge-886a2534a/

Licença
Distribuído sob a licença MIT – consulte o arquivo LICENSE para mais detalhes
