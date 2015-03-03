"""controller package"""
from general import GeneralController
from mouse import MouseController

controllers = {
    "GeneralController": GeneralController(),
    "MouseController": MouseController()
}
