import asyncio
from openai import AsyncOpenAI

from config import AITOKEN

client = AsyncOpenAI(api_key=AITOKEN, base_url="https://api.deepseek.com")

async def gpt_text(req, model='deepseek-chat'):
    try:
        competition = await client.chat.completions.create(
            messages=[{"role": "user", "content": str(req)}],
            model=model
        )
        return {'response': competition.choices[0].message.content,
                'usage': competition.usage.total_tokens}
    except Exception as e:
        print(f"Ошибка: {e}")
        return None


if __name__ == "__main__":
    # Добавьте принты для отладки
    print("Запуск генерации...")
    result = asyncio.run(gpt_text('ответь на вопрос - в чем сила?', 'deepseek-chat'))

    if result:
        print(f"Результат: {result}")
    else:
        print("Не удалось получить результат")