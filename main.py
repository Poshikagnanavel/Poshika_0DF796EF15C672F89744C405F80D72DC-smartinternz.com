#Define the basic class player 
class player:
  def play(self):
    print("The player is playing cricket.") 

# Define the derived class Batsman
class Batsman:
  def play(self):
     print("The batsman is batting.")
#Define the derived class Bowler
class Bowler:
  def play(self):
    print("The bowler is bowling.")
#Create objects of Batsman and Bouter classes
batsman = Batsman()
bowler =Bowler()
#Call the play sethod for each object
batsman.play()
bowler.play()