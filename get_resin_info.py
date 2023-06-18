import asyncio
import genshin

async def get_resin_info():
    lt_values_file = open(".env", "r").read()
    lt_values = lt_values_file.split("\n")
    ltuid = int(lt_values[0].split("=")[1].strip())
    ltoken = lt_values[1].split("=")[1].strip()
    genshin_UID = int(lt_values[2].split("=")[1].strip())
    starrail_UID = int(lt_values[3].split("=")[1].strip())

    cookies = {"ltuid": ltuid, "ltoken": ltoken} #hoyolabから取得

    client = genshin.Client(cookies)

    genshin_resin = await client.get_genshin_notes(genshin_UID) #UID
    starrail_resin = await client.get_starrail_notes(starrail_UID)
    return (genshin_resin.current_resin, starrail_resin.current_stamina)

    

#asyncio.run(main())