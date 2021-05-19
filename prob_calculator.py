import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        
        self.contents = list()
        for i, j in kwargs.items():
            while(j>0):
                self.contents.append(i)
                j -= 1
                
    def draw(self, num_balls):
        if num_balls > len(self.contents):
            return self.contents
        balls = []
        for i in range(num_balls):
            random_ball = random.randint(0,(len(self.contents)-1))
            balls.append(self.contents[random_ball])
            self.contents.remove(self.contents[random_ball])
        return balls
         
def experiment(hat,expected_balls, num_balls_drawn,num_experiments):
    experiment_count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors_gotten = hat_copy.draw(num_balls_drawn)
        for color in colors_gotten:
            if color in expected_copy:
                expected_copy[color] -= 1       
        if (all(x<=0 for x in expected_copy.values())):
            experiment_count += 1
    return experiment_count/num_experiments
