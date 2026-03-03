# Sistema Bancário CLI em Python

## Descrição

Este projeto consiste em um sistema bancário desenvolvido em Python com interface via linha de comando (CLI), aplicando os princípios da Programação Orientada a Objetos (POO).

A aplicação permite o gerenciamento de contas bancárias, incluindo criação de contas, depósitos, saques, transferências e consulta de saldo. Todas as operações seguem regras de negócio que simulam restrições reais de um sistema financeiro.

O principal objetivo do projeto é consolidar conceitos fundamentais de orientação a objetos, como encapsulamento, organização de responsabilidades e modelagem de domínio.

---

## Funcionalidades

O sistema oferece as seguintes operações:

* Criação de conta bancária
* Depósito de valores
* Saque com validações
* Transferência entre contas
* Consulta de saldo
* Persistência automática dos dados

---

## Regras de Negócio

### Cadastro de Contas

* Cada conta possui:

  * Número único
  * Nome do titular
  * Saldo inicial
  * Limite diário de saque configurável
* Não é permitido criar contas com número já existente.

### Depósito

* Apenas valores positivos são aceitos.
* O saldo é atualizado imediatamente após a operação.

### Saque

* O valor do saque não pode exceder:

  * O saldo disponível.
  * O limite diário de saque configurado para a conta.
* Valores inválidos são rejeitados.

### Transferência

* Permitida apenas entre contas existentes.
* Deve respeitar:

  * Saldo disponível.
  * Limite diário de saque.
* A operação é atômica: débito e crédito são realizados de forma consistente.

### Consulta de Saldo

* Exibe o saldo atual da conta selecionada.

---

## Persistência de Dados

O sistema utiliza um arquivo no formato JSON para armazenar as informações das contas.

* Os dados são carregados ao iniciar o programa.
* As alterações são salvas automaticamente.
* As contas permanecem registradas mesmo após o encerramento da aplicação.

---

## Requisitos Técnicos Atendidos

* Aplicação desenvolvida utilizando Programação Orientada a Objetos.
* Implementação de classe principal para modelagem da conta bancária.
* Manipulação de arquivos JSON para persistência.
* Interface totalmente baseada em linha de comando.
* Separação clara entre regras de negócio e interação com o usuário.

---

## Objetivo do Projeto

Este projeto demonstra a aplicação prática de:

* Modelagem orientada a objetos
* Encapsulamento de dados
* Validação de regras de negócio
* Persistência de dados estruturados
* Organização e estruturação de um sistema de domínio simples

O resultado é um sistema funcional, consistente e estruturado, que simula operações básicas de um ambiente bancário real por meio de uma interface de terminal.
