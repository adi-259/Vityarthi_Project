def add_result(results, name, score):
    results.append({"name": name, "score": score})

def leaderboard(results):
    return sorted(results, key=lambda item: item["score"], reverse=True)
