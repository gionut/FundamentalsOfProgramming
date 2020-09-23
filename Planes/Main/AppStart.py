from Presentation.UI import Console
from Business.services import ServicePlanes
from Infrastructure.repository import Repo
from Validators.validators import ValidatePlane
from Domain.entities import Plane, Point

repoPlayerPlanes = Repo()
repoComputerPlanes = Repo()

validatePlane = ValidatePlane()

servicePlayerPlanes = ServicePlanes(repoPlayerPlanes, repoComputerPlanes, validatePlane)
serviceComputerPlanes = ServicePlanes(repoComputerPlanes, repoPlayerPlanes, validatePlane)

#repoPlayerPlanes.add(Plane(Point('A', '3'), Point('C', '3')))
#repoPlayerPlanes.add(Plane(Point('C', '5'), Point('C', '7')))

#repoComputerPlanes.add(Plane(Point('A', '3'), Point('C', '3')))
#repoComputerPlanes.add(Plane(Point('C', '5'), Point('C', '7')))


ui = Console(servicePlayerPlanes, serviceComputerPlanes)

ui.run()
