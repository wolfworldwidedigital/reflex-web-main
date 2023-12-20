from pcweb.route import Route
from .advanced_guide import *
from .api_reference import *
from .components import *
from .component_lib import *
from .database import *
from .gallery import gallery
from .getting_started import *
from .hosting import *
from .recipes import *
from .library import library
from .styling import *
from .resources import resources
from .tutorial import *
from .wrapping_react import *
from .datatable_tutorial import *
from .assets import *
from .dynamic_rendering import *
from .pages import *
from .ui_overview import ui_overview
from .events import *
from .vars import *
from .substates import *
from .utility_methods import *
from .state_overview import state_overview
from .api_routes import *
from .client_storage import *
from .conditional_rendering import conditional_rendering
from .rendering_iterables import rendering_iterables

doc_routes = [r for r in locals().values() if isinstance(r, Route)]