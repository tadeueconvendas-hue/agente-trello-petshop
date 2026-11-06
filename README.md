# 🐾 Agente de Automação de Fluxo de Trabalho - Pet Shop Amigo Fiel

Projeto desenvolvido como parte do Desafio de Projeto **"Criando um Agente para Automatizar um Fluxo de Trabalho com Python"**, integrante da trilha **DXC - IA do Zero ao Primeiro Agente** na [DIO](https://dio.me).

---

## 📌 Visão Geral do Projeto
Este projeto implementa um agente autônomo em Python para automatizar o fluxo de atendimento e agendamento de serviços em um Pet Shop (banhos, tosas e consultas veterinárias). 

O agente interage com o cliente de forma amigável e se integra diretamente à API do **Trello**, automatizando a criação, a listagem e a transição de status das ordens de serviço.

---

## ⚙️ Fluxo de Trabalho Automatizado
1. **Atendimento Interativo:** Coleta de forma gentil os dados do tutor, do pet e o serviço desejado.
2. **Criação de Tarefa (Trello):** Cria automaticamente um cartão detalhado na lista **"A Fazer"** do quadro.
3. **Listagem de Agendamentos:** Consulta e exibe em tempo real as tarefas pendentes na lista.
4. **Movimentação Automática:** Conforme o status do atendimento avança, o agente move o cartão entre as listas:
   - `A Fazer` ➡️ `Em Andamento` ➡️ `Concluído`.

---

## 🛠️ Tecnologias Utilizadas
- **Python 3**
- **Requests:** Para consumo da API REST do Trello.
- **Python-dotenv:** Para gerenciamento seguro de variáveis de ambiente.
- **Trello API:** Plataforma de gerenciamento do fluxo Kanban.
- **Ambiente Virtual (venv):** Isolamento de dependências.

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
   cd SEU_REPOSITORIO
   ```

2. **Crie e ative o ambiente virtual:**
   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instale as dependências:**
   ```bash
   pip install requests python-dotenv
   ```

4. **Configure as Variáveis de Ambiente:**
   Crie um arquivo `.env` na raiz do projeto com as suas credenciais do Trello:
   ```env
   TRELLO_API_KEY=sua_api_key_aqui
   TRELLO_TOKEN=seu_token_aqui
   TRELLO_LIST_A_FAZER=id_da_lista_a_fazer
   TRELLO_LIST_EM_ANDAMENTO=id_da_lista_em_andamento
   TRELLO_LIST_CONCLUIDO=id_da_lista_concluido
   ```

5. **Execute o Agente:**
   ```bash
   python agente.py
   ```