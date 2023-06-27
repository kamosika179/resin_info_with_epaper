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

    genshin_info = await client.get_genshin_notes(genshin_UID) #UID
    starrail_info = await client.get_starrail_notes(starrail_UID)

    #genshin expedition and commition info
    genshin_finished_expedition_num = 0
    for i in genshin_info.expeditions:
        if i.status == "Finished":
            genshin_finished_expedition_num += 1
    
    is_genshin_expedition_finished = False
    if genshin_finished_expedition_num == genshin_info.max_expeditions:
        is_genshin_expedition_finished = True
    
    is_genshin_commission_finished = False
    if genshin_info.completed_commissions == genshin_info.max_commissions:
        is_genshin_commission_finished = True
    
    #starrail expedition and commition info
    starrail_finished_expedition_num = 0
    for i in starrail_info.expeditions:
        if i.status == "Finished":
            starrail_finished_expedition_num += 1
    
    is_starrail_expedition_finished = False
    if starrail_finished_expedition_num == starrail_info.total_expedition_num:
        is_starrail_expedition_finished = True

    is_starrail_commission_finished = True #本来False

    """
    #スターレイルのデイリー状況が取れないっぽい？のでTrueを返すようにしておきます。
    if starrail_info.completed_commissions == starrail_info.max_commissions:
        is_starrail_commission_finished = True
    """

    return (genshin_info.current_resin,is_genshin_expedition_finished,is_genshin_commission_finished,starrail_info.current_stamina,is_starrail_expedition_finished,is_starrail_commission_finished)

    
if __name__ == "__main__":
    print(asyncio.run(get_resin_info()))
