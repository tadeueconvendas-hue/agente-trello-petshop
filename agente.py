import os
import requests
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

API_KEY = os.getenv("TRELLO_API_KEY")
TOKEN = os.getenv("TRELLO_TOKEN")
ID_A_FAZER = os.getenv("TRELLO_LIST_A_FAZER")
ID_EM_ANDAMENTO = os.getenv("TRELLO_LIST_EM_ANDAMENTO")
ID_CONCLUIDO = os.getenv("TRELLO_LIST_CONCLUIDO")


def criar_agendamento_trello(nome_tutor, nome_pet, tipo_pet, servico, data, horario):
    """Cria um cartão na lista 'A fazer' do Trello com os dados do agendamento."""
    url = "https://api.trello.com/1/cards"
    
    titulo = f"🐾 {nome_pet} ({tipo_pet}) - {servico}"
    descricao = (
        f"**Tutor(a):** {nome_tutor}\n"
        f"**Pet:** {nome_pet} ({tipo_pet})\n"
        f"**Serviço:** {servico}\n"
        f"**Data e Horário:** {data} às {horario}\n"
        f"**Status:** Agendado via Agente Virtual"
    )
    
    params = {
        "key": API_KEY,
        "token": TOKEN,
        "idList": ID_A_FAZER,
        "name": titulo,
        "desc": descricao
    }
    
    resposta = requests.post(url, params=params)
    if resposta.status_code == 200:
        cartao = resposta.json()
        print(f"\n✅ Cartão criado no Trello com sucesso! (ID: {cartao['id']})")
        return cartao['id']
    else:
        print(f"\n❌ Erro ao criar no Trello: {resposta.status_code}")
        return None


def listar_agendamentos():
    """Lista todos os cartões na lista 'A fazer'."""
    url = f"https://api.trello.com/1/lists/{ID_A_FAZER}/cards"
    params = {"key": API_KEY, "token": TOKEN}
    
    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        cartoes = resposta.json()
        print("\n📋 AGENDAMENTOS NA LISTA 'A FAZER':")
        if not cartoes:
            print("Nenhum agendamento pendente no momento.")
        for idx, c in enumerate(cartoes, 1):
            print(f"{idx}. {c['name']}")
        return cartoes
    return []


def mover_agendamento(id_cartao, id_lista_destino, nome_destino):
    """Move um cartão para outra lista (ex: Em andamento ou Concluído)."""
    url = f"https://api.trello.com/1/cards/{id_cartao}"
    params = {
        "key": API_KEY,
        "token": TOKEN,
        "idList": id_lista_destino
    }
    
    resposta = requests.put(url, params=params)
    if resposta.status_code == 200:
        print(f"🚀 Agendamento movido para a lista '{nome_destino}' com sucesso!")
    else:
        print(f"❌ Erro ao mover cartão: {resposta.status_code}")


def executar_agente():
    print("=" * 55)
    print("🐾 BEM-VINDO(A) AO PET SHOP AMIGO FIEL! 🐾")
    print("Eu sou o Pipoca, seu assistente virtual de agendamentos. 🐶")
    print("=" * 55 + "\n")
    
    tutor = input("Como posso te chamar? ")
    print(f"\nPrazer, {tutor}! Vamos agendar o atendimento do seu pet.")
    
    pet = input("Qual o nome do seu pet? ")
    tipo_pet = input(f"O(A) {pet} é um cão, gato ou outro pet? ")
    
    print("\nEscolha o serviço desejado:")
    print("1 - Banho e Tosa 🛁✂️")
    print("2 - Consulta Veterinária 🩺")
    print("3 - Banho Simples 🧼")
    opcao = input("Digite o número (1, 2 ou 3): ")
    
    servicos = {"1": "Banho e Tosa", "2": "Consulta Veterinária", "3": "Banho Simples"}
    servico = servicos.get(opcao, "Atendimento Geral")
    
    data = input("\nQual dia fica melhor para você? (ex: Amanhã, 12/11): ")
    horario = input("E qual o melhor horário? (ex: 09:30, 15:00): ")
    
    print("\n" + "-" * 40)
    print("📋 RESUMO:")
    print(f"Tutor: {tutor} | Pet: {pet} ({tipo_pet})")
    print(f"Serviço: {servico} | Data: {data} às {horario}")
    print("-" * 40)
    
    confirma = input("\nPodemos confirmar e registrar na nossa agenda? (sim/não): ").strip().lower()
    
    if confirma in ["sim", "s"]:
        # 1. Agente cria o cartão no Trello
        id_cartao = criar_agendamento_trello(tutor, pet, tipo_pet, servico, data, horario)
        
        # 2. Agente lista as tarefas
        listar_agendamentos()
        
        # 3. Automação de movimentação de tarefas no Trello
        if id_cartao:
            print("\n" + "=" * 40)
            print("⚙️ SIMULAÇÃO DE FLUXO DE TRABALHO")
            print("=" * 40)
            avancar = input("\nO pet chegou na loja! Deseja mover para 'Em andamento'? (sim/não): ").strip().lower()
            if avancar in ["sim", "s"]:
                mover_agendamento(id_cartao, ID_EM_ANDAMENTO, "Em andamento")
                
                concluir = input("\nServiço finalizado! Deseja mover para 'Concluído'? (sim/não): ").strip().lower()
                if concluir in ["sim", "s"]:
                    mover_agendamento(id_cartao, ID_CONCLUIDO, "Concluído")
                    print("\n🎉 Fluxo de trabalho 100% concluído com sucesso!")
    else:
        print(f"\nAgendamento cancelado. Se precisar de algo mais, estou à disposição!")


if __name__ == "__main__":
    executar_agente()
    