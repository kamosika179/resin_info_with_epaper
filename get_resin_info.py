import asyncio
import genshin

async def main():
    #ファイルからクッキーを読み込む。一行ずつ読み出す
    lt_values_file = open(".env", "r").read()
    lt_values = lt_values_file.split("\n")
    ltuid = int(lt_values[0].split("=")[1].strip())
    ltoken = lt_values[1].split("=")[1].strip()

    cookies = {"ltuid": ltuid, "ltoken": ltoken} #仮で入れているが、外部に保存するようにすること

    client = genshin.Client(cookies)

    data = await client.get_genshin_notes(801029084)
    print(data.current_resin)
    

asyncio.run(main())