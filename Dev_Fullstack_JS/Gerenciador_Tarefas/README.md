# Minhas tarefas

Aplicação de lista de tarefas feita com HTML, CSS e JavaScript puro. O projeto oferece uma forma simples de registrar tarefas do dia, acompanhar o que já foi concluído e remover itens que não são mais necessários.

## Objetivo

Este projeto demonstra a construção de uma aplicação web pequena e funcional sem frameworks, bibliotecas ou serviços externos. A interface reúne um formulário para adicionar tarefas e uma lista atualizada dinamicamente no navegador.

As tarefas são mantidas em um array JavaScript enquanto a página está aberta. Isso deixa o funcionamento fácil de acompanhar, mas significa que os dados não são preservados ao recarregar ou fechar a página.

## Funcionalidades

- Adicionar tarefas por meio do campo de texto e do botão **Adicionar**.
- Remover espaços em branco no início e no fim do texto antes de registrar a tarefa.
- Impedir o cadastro de tarefas vazias.
- Criar cada nova tarefa com o estado inicial de não concluída.
- Marcar uma tarefa como concluída e desfazer essa ação posteriormente.
- Aplicar um estilo riscado ao texto das tarefas concluídas.
- Excluir tarefas da lista.
- Atualizar a quantidade de tarefas, incluindo a forma singular para uma tarefa.
- Exibir uma mensagem quando a lista estiver vazia.
- Ajustar a apresentação para telas menores.

## Tecnologias utilizadas

### HTML5

O arquivo `index.html` define a estrutura e o conteúdo da página. Ele utiliza elementos semânticos, como `main`, `header`, `section`, `form` e `ul`, além de rótulos e atributos ARIA para facilitar a navegação e a compreensão da interface.

O documento carrega os recursos locais:

```html
<link rel="stylesheet" href="assets/style.css">
<script src="assets/script.js" defer></script>
```

O atributo `defer` faz com que o JavaScript seja executado depois que o HTML for interpretado.

### CSS3

O arquivo `assets/style.css` cuida da apresentação visual, sem depender de bibliotecas. Entre os recursos usados estão:

- variáveis e seletores CSS;
- Flexbox e Grid para organizar formulários e tarefas;
- cores, espaçamentos, bordas arredondadas e sombras para os cards;
- estados de foco e interação dos controles;
- uma media query para adaptar o layout a telas estreitas.

O fundo cinza-claro, os cards brancos e os botões verdes seguem a proposta visual do projeto.

### JavaScript

O arquivo `assets/script.js` controla o comportamento da aplicação com JavaScript padrão do navegador:

- seleciona os elementos da interface no início do arquivo;
- registra interações usando `addEventListener`, sem manipuladores de eventos no HTML;
- mantém as tarefas em um array de objetos;
- atualiza a lista e o contador a partir dos dados atuais;
- usa `textContent` para inserir o texto da tarefa como conteúdo, em vez de interpretá-lo como HTML.

O formato de cada item é:

```js
{
    text: "Exemplo de tarefa",
    completed: false
}
```

Não são usados frameworks, pacotes npm, banco de dados ou API.

## Estrutura do projeto

```text
Projeto_Gerenciador_Tarefas/
├── assets/
│   ├── script.js
│   └── style.css
├── docs/
│   └── plan.md
├── index.html
└── README.md
```

| Arquivo | Responsabilidade |
| --- | --- |
| `index.html` | Estrutura da página, formulário e lista de tarefas. |
| `assets/style.css` | Estilos, estados visuais e adaptação para telas menores. |
| `assets/script.js` | Cadastro, renderização, conclusão, exclusão e contador. |
| `docs/plan.md` | Plano original e requisitos do projeto. |

## Como executar

O projeto não requer instalação de dependências nem etapa de compilação.

1. Baixe ou clone o repositório.
2. Abra a pasta `Projeto_Gerenciador_Tarefas`.
3. Abra `index.html` em um navegador.

Também é possível abrir a pasta no Visual Studio Code e usar uma extensão de servidor local, como o Live Server, para visualizar a página.

## Como usar

1. Digite uma tarefa no campo **Digite uma nova tarefa...**.
2. Selecione **Adicionar** para incluí-la na lista.
3. Use **Concluir** para marcar a tarefa. O texto ficará riscado e o botão passará a permitir desfazer a conclusão.
4. Use **Deletar** para remover a tarefa.
5. O contador e a mensagem da lista vazia são atualizados automaticamente.

## Armazenamento e limitações

Os dados existem apenas em memória, no array `tasks` do JavaScript. Portanto:

- atualizar a página limpa a lista;
- fechar a aba ou o navegador também elimina as tarefas;
- não há sincronização entre dispositivos ou navegadores.

Persistência em `localStorage`, contas de usuário e sincronização com um servidor não fazem parte do escopo atual.
