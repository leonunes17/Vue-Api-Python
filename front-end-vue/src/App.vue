<template>

  <div class="body">
      <div class="main">
          <div class="content">
              <img src="./assets/logo_intuitive.jpg" alt="logo_intuitive">
            <div class="inputs">
              <input type="text" v-model="query" placeholder="Digite a razão social..."/>
              <input class="button" type="submit" @click="search" :disabled="!query.trim()" value="Search"> 
            </div>
          </div>
      </div>
      <ul v-if="resultadoBusca.length > 0">
        <li v-for="item in resultadoBusca" :key="item.Registro_ANS" class="item">
          {{ item.Razao_Social }} | {{ item.Registro_ANS }} | {{ item.Cidade }} | {{ item.UF }}
        </li>
      </ul>
  </div>
  
  </template>
  
  <script>
  export default {
  
    data() {
      return {
        default_URL: "http://localhost:5000/search?query=",   //url base para busca
        query: '',                                            //query de busca digitada no input
        resultadoBusca: [],                                   //resultado da busca no csv
      };
    },
  
    methods: {
      search() { 
        if (this.query.trim()) {
  
          const fullURL = `${this.default_URL}${this.query}`; //juntando a url base com a query do input 
  
          fetch(fullURL) 
            .then(response => response.json())
            .then(data => {
              this.resultadoBusca = data; 
            })
            .catch(error => {
              console.error('Error fetching data:', error);
            });
        }
      }
    },
  };
  </script>
  
  <style scoped>
  
  .body {
      display: flex;
      align-items: center;
      margin-top: 5rem;
      flex-direction: column;
      font-family: 'Lucida Sans', sans-serif;
  }
  
  .main {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 35rem;
      height: 10rem;
      background: transparent;
      border: 1px solid rgb(219, 126, 253);
      border-radius: .5rem;
      box-shadow: 0px 8px 10px rgba(0, 0, 0, .5);
  }
  
  .content img{
      margin-left: 8rem;
  }
  
  
  input {
      font-size: 1.3rem;
      border-radius: .5rem;
      border-color: rgb(219, 126, 253, .7);
      padding: .5rem;
      width: 25rem;
      font-family: 'Lucida Sans', sans-serif;    
  }
  
  .button {
      color: white;
      width: 6rem;
      font-size: 1.3rem;
      font-weight: 400;
      padding: .5rem;
      border-radius: .5rem;
      border-color: rgb(33, 33, 33);
      background-color: rgb(219, 126, 253);
      cursor: pointer;
      margin-left: .2rem;
  }
  
  .button:hover{
      color: rgb(219, 126, 253);
      background-color: rgb(33, 33, 33);
      transition: .5s;
  }
  
  ul{
      width: 32rem;
      max-height: 15rem;
      overflow: auto;
      list-style: none;
      border: 1px solid rgb(219, 126, 253);
      border-radius: .5rem;
      background: transparent;
      padding: 1.5rem;
      margin-top: 2rem;
      box-shadow: 0px 8px 10px rgba(0, 0, 0, .5);
  }
  
  li{
    font-size:1.1rem
  }
  
  .item{
    padding: .5rem;
  }
  
  </style>