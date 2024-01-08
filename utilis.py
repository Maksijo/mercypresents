import openai
import logging
import config

openai.api_key = config.OPENAI_TOKEN

async def generated_text(promt) -> dict:
    try:
        response = await openai.ChatCompletion.acreate(
            model = "gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": promt}
            ]
        )
        return response['choices'][0]['message']['content'], response['usage']['total_tokens']
    except Exception as e:
        logging.error(e)

async def generate_image(promt, n=1, size="1024x1024") -> list[str]:
    try:
        response = await openai.Image.acreate(
            promt=promt,
            n=n,
            size=size
        )
        urls = []
        for i in response['data']:
            urls.append(i['url'])
    except Exception as e:
        logging.error(e)
        return []
    else:
        return urls