def get_result(final_score):
    if final_score["Home score"] > final_score["Away score"]:
        return "Home win"
    elif final_score["Home score"] < final_score["Away score"]:
        return "Away win"
    else:
        return "Draw"

def get_results(final_scores):
    results = [get_result(score) for score in final_scores]
    return results
    # (You could try and use a list comprehension for this)
