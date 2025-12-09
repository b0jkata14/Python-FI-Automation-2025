def compute_final_score(*scores, **rules):
    penalty = rules.get("penalty", 0)
    bonus_func = rules.get("bonus_func", None)

    def adjust(score):
        result = score - penalty

        if result < 0:
            result = 0

        return result

    adjusted_scores = map(adjust, scores)

    total = sum(adjusted_scores)

    if bonus_func is not None:
        total = bonus_func(total)

    return total

