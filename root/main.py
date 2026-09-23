import utils
import score
from utils import generate_secret_number, check_user_guess
from score import loss_of_score, score_rating, at_specific_lowscore

score = 100

secret_number = utils.generate_secret_number()

while True:
    if utils.check_user_guess(secret_number):
        print(f"Final Score is: {score}")
        score_rating(score)
        break
    else:
        score = loss_of_score(score)
        print(f"Score: {score}")
        at_specific_lowscore(score)