# 🔎 Buscador de Repositórios no GitHub

## 📌 Sobre o projeto

O **Buscador de Repositórios no GitHub** é uma aplicação web que permite pesquisar repositórios públicos diretamente no GitHub por meio de palavras-chave.

A aplicação consome a API oficial do GitHub e apresenta os resultados de forma organizada, exibindo informações como nome do repositório, autor, descrição, linguagem principal e quantidade de estrelas.

O projeto tem como objetivo praticar conceitos de desenvolvimento Front-end, consumo de APIs externas e manipulação do DOM com JavaScript.

## 🚀 Funcionalidades

- Pesquisa de repositórios por palavra-chave.
- Busca realizada somente ao pressionar ENTER.
- Exibição de até 10 repositórios por pesquisa.
- Resultados ordenados pela quantidade de estrelas.
- Exibição do nome e foto do autor.
- Exibição do nome e descrição do repositório.
- Exibição da linguagem principal utilizada.
- Exibição da quantidade de estrelas.
- Link direto para acessar o repositório no GitHub.
- Indicador de carregamento (Loading State).
- Mensagem quando nenhum resultado é encontrado (Empty State).
- Mensagem amigável em caso de erro.

## 🛠️ Tecnologias utilizadas

- **HTML5:** estruturação da aplicação.
- **CSS3:** estilização, layout e responsividade.
- **JavaScript:** lógica da aplicação, manipulação do DOM e gerenciamento de eventos.
- **Fetch API:** realização de requisições HTTP.
- **Async/Await:** gerenciamento de operações assíncronas.
- **GitHub REST API:** fornecimento dos dados dos repositórios.

## 🔗 API utilizada

O projeto utiliza a API oficial do GitHub para realizar as pesquisas.

**Endpoint:**

```text
https://api.github.com/search/repositories?q={PALAVRA-CHAVE}&sort=stars&per_page=10
```

**Parâmetros:**

| Parâmetro | Descrição |
|---|---|
| `q` | Palavra-chave da pesquisa. |
| `sort=stars` | Ordena os resultados por estrelas. |
| `per_page=10` | Limita a resposta a 10 repositórios. |

## ⚙️ Funcionamento

1. O usuário digita uma palavra-chave no campo de pesquisa.
2. Ao pressionar ENTER, o JavaScript captura o evento.
3. A aplicação exibe o indicador de carregamento.
4. Uma requisição é realizada utilizando Fetch API.
5. Os dados retornados são processados e exibidos na tela.
6. Caso não existam resultados, uma mensagem informativa é apresentada.
7. Caso ocorra algum erro, uma mensagem amigável é exibida.

As requisições utilizam `async/await`, `try/catch` e verificação do status HTTP da resposta.

Todos os eventos são registrados diretamente no JavaScript, sem utilização de eventos inline no HTML.

## 🎨 Interface

A aplicação possui uma interface simples e intuitiva, com:

- Conteúdo centralizado na página.
- Largura máxima de 700px.
- Fundo escuro para destacar os cards.
- Card de pesquisa com bordas arredondadas.
- Card de resultados com bordas arredondadas.
- Organização visual das informações dos repositórios.

## 📂 Estrutura do projeto

```text
buscador-github/
│
├── index.html
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
└── README.md
```

## ▶️ Como executar o projeto

1. Clone o repositório:

```bash
git clone URL_DO_REPOSITORIO
```

2. Entre na pasta do projeto:

```bash
cd buscador-github
```

3. Abra o arquivo `index.html` no navegador ou utilize a extensão Live Server do VS Code.

4. Digite uma palavra-chave no campo de pesquisa e pressione ENTER.

## 🎯 Objetivo de aprendizado

Este projeto foi desenvolvido para praticar conceitos fundamentais do desenvolvimento Front-end:

- Manipulação do DOM.
- Captura e gerenciamento de eventos.
- Consumo de APIs REST.
- Requisições HTTP com Fetch API.
- Programação assíncrona com Async/Await.
- Tratamento de erros com Try/Catch.
- Desenvolvimento de interfaces web.

---

Desenvolvido com 💻 e ☕ para praticar e evoluir no desenvolvimento web.
````

Como salvar: copie o conteúdo acima, crie um arquivo chamado `README.md` na pasta principal do projeto e cole o conteúdo nele.