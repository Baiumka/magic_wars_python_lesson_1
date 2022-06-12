from Skill import *

fire_skill = FireSkill(100, "Fire.png", "Огонь", 0, 0)
water_skill = WaterSkill(100, "Water.png", "Вода", 100, 0)
wind_skill = WindSkill(100, "Wind.png", "Воздух", 200, 0)
earth_skill = EarthSkill(100, "Earth.png", "Земля", 300, 0)
base_skill_list = [fire_skill, water_skill, wind_skill, earth_skill]


steam_skill = SteamSkill(100, "Steam.png", "Пар", 0, 0)



def check_combination(spell_list):
    if fire_skill in spell_list and water_skill in spell_list:
        return steam_skill




    return None
