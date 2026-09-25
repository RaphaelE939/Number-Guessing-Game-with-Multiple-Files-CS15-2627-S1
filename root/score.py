def loss_of_score(score):
        score -= 10
        if score < 0:
            score = 0
        return score

def at_specific_lowscore(score):
    if score <= 10:
        print("Don't get any more wrong or else you lose.")
    elif score < 1:
        print("You have lost all your points...You lose.")

def score_rating(score):
    if score > 99:
        print("...How?")
    elif score > 79:
        print("Wow, you are not terrible")
    elif score > 49:
        print("At least you passed...")
    elif score >= 0:
        print("WOW... I don't mean that in a good way. You BETTER keep practicing")

if __name__ == "__main__":
    score_rating(100)