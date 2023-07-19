from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton

from designer_backend.backend_server.designer_server.adapter.repository.out_repository import OutRepository
class BaseContainer(DeclarativeContainer):
    """Base container."""

    config = Configuration()

    login_hrm_out_port = Singleton(OutRepository.LoginHrmApiAdapter)
