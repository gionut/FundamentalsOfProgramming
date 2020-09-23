from Ui import Console
from Controller import PlayerController, ComputerController
from Validators import Validate
from Repository import Repo

validate = Validate()
repoPoints = Repo()
repoCPoints = Repo()


playerController = PlayerController(validate, repoPoints)
computerController = ComputerController(validate, repoCPoints)

console = Console(playerController, computerController)

console.run()