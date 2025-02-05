def solution(picks, minerals):
    total_picks = sum(picks)
    max_minerals = total_picks * 5 

    minerals = minerals[:max_minerals]
    
    mineral_groups = []
    for i in range(0, len(minerals), 5):
        group = minerals[i:i+5]
        dia, iron, stone = group.count("diamond"), group.count("iron"), group.count("stone")
        mineral_groups.append((dia, iron, stone))
    
    mineral_groups.sort(reverse=True, key=lambda x: (x[0], x[1], x[2]))

    groups_to_process = mineral_groups[:total_picks]
    
    fatigue_table = {
        "diamond": [1, 1, 1],
        "iron": [5, 1, 1],
        "stone": [25, 5, 1]
    }

    fatigue = 0
    for (dia, iron, stone) in groups_to_process:
        if picks[0] > 0:
            pick_type = "diamond"
            picks[0] -= 1
        elif picks[1] > 0:
            pick_type = "iron"
            picks[1] -= 1
        else:
            pick_type = "stone"
            picks[2] -= 1
        
        fatigue += (
            fatigue_table[pick_type][0] * dia +
            fatigue_table[pick_type][1] * iron +
            fatigue_table[pick_type][2] * stone
        )
    
    return fatigue
