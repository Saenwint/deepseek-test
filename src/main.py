import ollama
import logging
import time
import re

import tests.test_deepseek as tests

# Настройка логирования
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('src/chat.md', mode='w'),
        logging.StreamHandler()
    ]
)

model = 'deepseek-r1:1.5b'

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"},
]

while True:
    user_prompt = input("USER: ")
    if not user_prompt:
        break  # пустой ввод завершает цикл

    if "task leetcode" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_leetcode()}"})
    elif "unittest" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_unittest()}"})
    elif "integral" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_integral()}"})
    elif "equation" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_equation()}"})
    elif "correct sentence" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_sentence_correct()}"})
    elif "poem" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_write_poem()}"})
    elif "story" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_write_story()}"})
    elif "retelling" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_retelling_text()}"})
    elif "cross" in user_prompt.lower():
        messages.append({"role": "user", "content": f"{user_prompt}\n\n{tests.test_cross_text()}"})
    elif "stress test" in user_prompt.lower():
        num_requests = 20  # Количество запросов
        prompt = "x = 3*3*3. Find x"
        avg_time, error_count = tests.stress_test(num_requests, prompt)
        print(f"Среднее время обработки: {avg_time:.2f} секунд")
        print(f"Количество ошибок: {error_count}")
        continue  # Пропускаем обычную обработку запроса
    else:
        messages.append({"role": "user", "content": user_prompt})

    # Замер времени начала обработки запроса
    start_time = time.time()

    response = ollama.chat(
        model=model,
        messages=messages,
    )

    # Замер времени окончания обработки запроса
    end_time = time.time()

    answer = response['message']['content']

    # Удаление секции <think> из ответа
    answer = re.sub(r'<think>.*?</think>', '', answer, flags=re.DOTALL).strip()

    print("DeepSeek:", answer)
    messages.append({"role": "assistant", "content": answer})

    # Логирование времени обработки и сообщений
    processing_time = end_time - start_time
    logging.info(f"USER: {user_prompt}")
    logging.info(f"DeepSeek: {answer}")
    logging.info(f"Processing time: {processing_time:.2f} seconds\n")