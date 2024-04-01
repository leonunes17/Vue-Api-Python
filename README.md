# Flask API para Pesquisa em Relatório CADOP

Este código consiste em uma API Flask simples que permite realizar pesquisas em um conjunto de dados do Relatório CADOP, que é carregado a partir de um arquivo CSV. Abaixo está uma explicação detalhada do código:

## Dependências

- Flask: Uma estrutura leve para construir aplicativos web em Python.
- pandas: Uma biblioteca de software escrita como extensão da linguagem Python para manipulação e análise de dados.
- flask_cors: Uma extensão do Flask que simplifica o suporte ao Cross-Origin Resource Sharing (CORS).

## Funcionamento

1. O código inicializa um aplicativo Flask e ativa o suporte ao CORS para permitir solicitações de diferentes origens.
2. Carrega os dados do Relatório CADOP a partir de um arquivo CSV usando a biblioteca pandas.
3. Define uma rota `/search` que aceita solicitações GET para realizar pesquisas no conjunto de dados.
4. Na função de rota `search()`, obtém a consulta de pesquisa dos parâmetros da solicitação.
5. Filtra os dados com base na consulta de pesquisa fornecida e converte os resultados para um formato JSON.
6. Retorna os resultados da pesquisa em formato JSON.
7. O aplicativo Flask é executado em modo de depuração se o script for executado diretamente.

Este README fornece uma visão geral do funcionamento da API Flask para pesquisa em um conjunto de dados do Relatório CADOP. Certifique-se de fornecer o caminho correto para o arquivo CSV e ajustar a lógica da pesquisa conforme necessário para atender aos requisitos do seu projeto.

# Componente Vue.js para Interface de Pesquisa

Este código consiste em um componente Vue.js para construir uma interface de pesquisa que interage com a API Flask descrita anteriormente. Abaixo está uma explicação detalhada do código:

## Funcionamento

1. O componente Vue.js consiste em um formulário com um campo de entrada para a pesquisa e um botão de envio.
2. Quando o botão de envio é clicado, uma solicitação GET é enviada para a rota `/search` da API Flask, passando a consulta de pesquisa como parâmetro.
3. Os resultados da pesquisa são exibidos em uma lista abaixo do formulário.
4. O estilo do componente Vue.js é definido usando estilos CSS no próprio componente.

Este README fornece uma visão geral do componente Vue.js para construir uma interface de pesquisa que interage com a API Flask. Certifique-se de configurar corretamente a URL base da API e ajustar o estilo conforme necessário para se adequar ao seu projeto.

## Resultados de Busca

![resultado_busca1](https://github.com/leonunes17/Vue-Api-Python/assets/96439824/5561d895-818b-4538-9354-bb4a9ca4e851)
![resultado_busca2](https://github.com/leonunes17/Vue-Api-Python/assets/96439824/bef53db6-5c62-47db-ac1c-1adbc04d9f34)

# Postman Collection

Esta coleção do Postman foi criada para testar uma solicitação GET em uma API Flask que realiza uma pesquisa baseada em consulta.

## Informações da Coleção

- **ID do Postman:** 6ed85fee-ed86-4cbf-9ea4-c9e90352d05a
- **Nome:** New Collection
- **Schema:** [Collection v2.1.0](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)
- **ID do Exportador:** 33907383

## Itens

- **Nome:** New Request
- **Método:** GET
- **URL:** `http://localhost:5000/search?query=anafe`
- **Descrição:** Este item representa uma solicitação GET para a rota `/search` de uma API Flask. Ele inclui uma consulta de pesquisa com o valor "anafe".

### Observações

Esta coleção do Postman é útil para testar a funcionalidade de pesquisa da API Flask. Você pode usar esta coleção para realizar solicitações de teste e verificar se a API está respondendo corretamente com os resultados esperados.

Certifique-se de ajustar a URL da solicitação de acordo com a configuração da sua API Flask e o valor da consulta de pesquisa conforme necessário para os seus testes.
