from getpass import getpass
from gigachat import GigaChat
from gigachat.models import ChatCompletionRequest, ChatMessage

key = getpass("Введите ключ: ")

# 1. Начало диалога
messages = [
    ChatMessage(role="system", content="Ты учебный помощник. Пиши простыми словами.")
]

# --- ПЕРВЫЙ ВОПРОС ---
user_text_1 = input("Вы (вопрос 1): ")
messages.append(ChatMessage(role="user", content=user_text_1))

# Отправляем первый запрос
request_1 = ChatCompletionRequest(messages=messages)

with GigaChat(
    credentials=key, 
    verify_ssl_certs=False, 
    model="GigaChat-2",
    max_retries=3, 
    timeout=60.0
) as client:
    response_1 = client.chat.create(request_1)
    answer_1 = response_1.messages[0].content[0].text
    print("\nБот:", answer_1)

    # СОХРАНЯЕМ ОТВЕТ БОТА В ИСТОРИЮ
    messages.append(ChatMessage(role="assistant", content=answer_1))

    # --- ВТОРОЙ ВОПРОС (зависит от первого) ---
    # Например, если первый вопрос был про списки, второй спрашивает про добавление в них
    user_text_2 = input("\nВы (вопрос 2, зависит от первого): ")
    messages.append(ChatMessage(role="user", content=user_text_2))

    # Отправляем второй запрос (с полной историей!)
    request_2 = ChatCompletionRequest(messages=messages)
    response_2 = client.chat.create(request_2)
    answer_2 = response_2.messages[0].content[0].text
    print("\nБот:", answer_2)