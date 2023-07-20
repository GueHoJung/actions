from .base_container import BaseContainer
from . import settings

container = BaseContainer()
container.config.from_dict(settings.__dict__)
