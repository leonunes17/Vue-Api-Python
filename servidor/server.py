from flask import Flask, request
import pandas as pd                        
from flask_cors import CORS

app = Flask(__name__)

CORS(app) #CORS necessário para permissão de solicitações de diferentes origens

data = pd.read_csv('Relatorio_cadop.csv', delimiter=';') #definindo um dataframe que recebe os dados do arquivo csv

@app.route('/search', methods=['GET']) 
def search():

    query = request.args.get('query') #obtendo a variavel de pesquisa 

    new_data = data[data['Razao_Social'].str.contains(query, case=False)] #definindo um novo dataframe com o filtro

    new_data = new_data.where(pd.notna(new_data), None) #transformando campos NaN em None (prevenção de erro do Json)

    new_data_json = new_data.to_dict(orient='records') #transformando o dataframe em dicionario do python

    new_data_json = new_data.to_json(orient='records', date_format='iso', default_handler=str) #transformando o dataframe em json

    return new_data_json #retornado o dataframe final
    
if __name__ == '__main__':  #inicialização do app flask
    app.run(debug=True)