from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# 1. Instanciando o robô
# Se o banco de dados 'db.sqlite3' não existir, ele será criado automaticamente.

bot = ChatBot("AssistenteSENAI", read_only=False)



# -------------------------------------------------------------
# 2. Treinando o Chatbot com Perguntas e Respostas Personalizadas
# -------------------------------------------------------------
trainer_lista = ListTrainer(bot)

# Lista com o diálogo de treino (Pergunta -> Resposta)
conversa_customizada = [
    "Olá",
    "Olá! Como posso ajudar você hoje?",
    "Quais cursos você oferece?",
    "Oferecemos cursos de Inteligência Artificial, Programação e Banco de Dados.",
    "Qual a duração do curso de IA?",
    "O curso de IA tem carga horária de 48 horas.",
    "Obrigado",
    "Por nada! Estou à disposição.",
]

# Executa o treino com a lista
trainer_lista.train(conversa_customizada)

# -------------------------------------------------------------
# 3. Treinando com Diálogos Prontos em Português (Opcional)
# -------------------------------------------------------------
trainer_corpus = ChatterBotCorpusTrainer(bot)

# Treina com saudações em português
trainer_corpus.train("chatterbot.corpus.portuguese.greetings")

# -------------------------------------------------------------
# 4. Criando o Loop de Conversa no Terminal
# -------------------------------------------------------------
print("\n🤖 Chatbot Pronto! Digite 'sair' para encerrar a conversa.\n")

while True:
    # Captura a pergunta digitada pelo usuário
    pergunta = input("Você: ")

    # Verifica se o usuário quer encerrar o programa
    if pergunta.lower().strip() in ["sair", "exit", "quit"]:
        print("🤖 AssistenteSENAI: Até logo e bons estudos!")
        break

    # O robô calcula a melhor resposta na base de dados
    resposta = bot.get_response(pergunta)

    # Exibe a resposta na tela
    print(f"🤖 AssistenteSENAI: {resposta}\n")

with open("dados_conversa.txt", encoding='utf-8') as arquivo:
    for linha in arquivo:
        pergunta, resposta = linha.strip().capitalize().split(" -> ")
        bot.storage.create(
            text=pergunta,
            in_response_to=[resposta]
)


