from Repository import RepoShips
from Validators import ValidateShip, ValidatePoint
from ShipsController import ShipController
from Domain import Ship, Point
from Ui import Console

repoShips = RepoShips()
repoComputer = RepoShips()
#repoShips.add(Ship(Point('A', '1'), Point('A','2'), Point('A', '3')))
#repoShips.add(Ship(Point('D', '1'), Point('D','2'), Point('D', '3')))

validateShip = ValidateShip()
validatePoint = ValidatePoint()

shipController = ShipController(repoShips, validateShip, validatePoint)
computerController = ShipController(repoComputer, validateShip, validatePoint)

console = Console(shipController, computerController)

console.run()