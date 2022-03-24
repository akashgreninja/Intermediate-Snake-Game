import turtle
from  turtle import Turtle,Screen
import random
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

score=0
end_positions=[]
screen=Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.tracer(0)




snake=Snake()

food=Food()
scoreboard=ScoreBoard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

end_game=False

while end_game==False:
    screen.update()
    time.sleep(0.15)
    snake.move()

# detect collision

    if snake.head.distance(food) < 15:
        # score += 1
        scoreboard.increasescore()



        food.refresh()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor()< -280 or snake.head.ycor()> 280 or snake.head.ycor() < -280:
        # end_game=True
        scoreboard.restart()
        # scoreboard.game_over()
        snake.reset()

    def restart():
        end_game=False


    # screen.onkey(restart, "w")
    for segments in snake.all_turtles[1:]:

        if snake.head.distance(segments)<10:
            # end_game=True
            scoreboard.restart()
            snake.reset()
            # scoreboard.game_over()


        # if screen.onkey(restart, "w"):
        #     end_game=False


#Main principal here is the last block should move to the block before it and so on

























screen.exitonclick()