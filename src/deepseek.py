from datetime import datetime
import re
import ollama
import os

model = "deepseek-r1:1.5b"
input_folder = "src/prompts"

def read_prompts_from_file(filename):
    """Читает запросы из файла"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            prompts = content.split("EndOfPromt")
            prompts = [prompt.strip() for prompt in prompts if prompt.strip()]
            return prompts
    except FileNotFoundError:
        return (f"Файл {filename} не найден.")
    except Exception as e:
        return (f"Ошибка при чтении файла: {e}")

try:
    files = os.listdir(input_folder)
except FileNotFoundError:
    print(f"Папка {input_folder} не найдена.")
    exit()

prompt_files = [f for f in files if f.endswith("_prompt.txt")]

if not prompt_files:
    print("Нет файлов с запросами для обработки.")
else:
    for prompt_file in prompt_files:
        file_path = os.path.join(input_folder, prompt_file)
        print(f"Обработка файла: {file_path}")
        
        prompts = read_prompts_from_file(file_path)
        
        if not prompts:
            print(f"Файл {file_path} не содержит запросов.")
            continue
        
        for my_prompt in prompts:
            print(f"Обработка запроса: {my_prompt}")

            answer = ollama.generate(model=model, prompt=my_prompt) 
            response = answer["response"]
            response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()

            with open("src/chat.md", "a", encoding="utf-8") as f:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f.write(f"[{timestamp}]\n")
                f.write(f"**You:** {my_prompt}\n")
                f.write(f"**DeepSeek:** {response}\n" + "\n")
                f.write("-" * 50 + "\n")
                f.write(f"model: {answer['model']}\n")
                f.write(f"created_at: {answer['created_at']}\n")
                f.write(f"total_duration: {answer['total_duration']/10**9}sec\n")
                f.write(f"load_duration: {answer['load_duration']/10**9}sec\n")
                f.write(f"prompt_eval_count: {answer['prompt_eval_count']}\n")
                f.write(f"prompt_eval_duration: {answer['prompt_eval_duration']/10**9}sec\n")
                f.write(f"Token/s: {answer['eval_count']/answer['eval_duration']*10**9}\n")
                f.write("-" * 50 + "\n\n")