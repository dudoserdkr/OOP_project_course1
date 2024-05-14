from Coin import Coin
from Score import Score

coin = Coin()
score = Score()

coin.add_observer(Score)

coin.flip()