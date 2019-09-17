from random import randint
from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route('/')
# changed from ('/index.html')
def play_dice_game():
    # roll = input("Roll the dice? [Y or N]")
    # running = True
    # play = ""
    # while running == True:
    #     if play.upper() == "Y":
    #         print("You will rolling two 6-sided dice")
    #         print("If you roll the same number on both, you win!")
    #     else:
    #         print("Thank you. Have a nice day.")
    #         running = False
    message = ""
    dice_1 = randint(1,6)
    dice_2 = randint(1,6) 
    # variables dice_1 and dice_2 each contain a number between 1 and 6
    result = [dice_1, dice_2, message]
    if dice_1 == dice_2:
        message = "WIN"
    else:
        message = "LOSE"
        
    result = "Dice One was " + str(dice_1) + " and Dice Two was " + str(dice_2) + ". You " + message

    print(result)

    # return result
    return render_template("dice.html", dice_1 = dice_1, dice_2 = dice_2)

if __name__ == "__main__":
   app.run(debug=True)
