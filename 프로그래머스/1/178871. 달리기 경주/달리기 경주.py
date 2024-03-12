def solution(players, callings):
    ranking = {name:rank for rank, name in enumerate(players)}
    for name in callings:
        rank = ranking[name]
        ranking[name] -= 1
        ranking[players[rank-1]] += 1
        players[rank-1], players[rank] = name, players[rank-1] 
    return players