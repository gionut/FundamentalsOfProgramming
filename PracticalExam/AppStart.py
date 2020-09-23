from Ui import Console
from Controller import Controller
from Repository import Repo
from Validators import Validate


repoGame = Repo()
validate = Validate()


controller = Controller(repoGame, validate)

console = Console(controller)

console.run()