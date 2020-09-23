from Ui import Console
from Controller import GameControler
from Repository import Repo
from Validate import Validate

repoGame = Repo()
validate = Validate()

gameController = GameControler(repoGame, validate)

console = Console(gameController)

console.run()