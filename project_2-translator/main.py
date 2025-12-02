from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

# Article
article = "自動車のＦ１世界選手権に参戦しているレッドブルは２日、来季のレギュラードライバーを発表し、今季途中から加わった角田裕毅（２５）は外れ、テスト兼リザーブドライバーになることが決まった。レギュラードライバー２人は、エースのマックス・フェルスタッペン（オランダ）と、傘下のレーシングブルズから昇格する２１歳のイザック・アジャー（仏）が務める。"

# Prompt
prompt = f"Translate the following article: {article}"


# Create a function that can translate the article
def article_translator(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role":"user", "content":prompt},
                  {"role":"assistant","content":"You are a professional translator. You translate news articles into English"},
                  {"role":"system", "content":"Direct english translator"}],
        temperature=0.1
    )
    return response.choices[0].message.content


# return the translated article
print(article_translator(prompt))