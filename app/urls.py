
from fastapi import Path
import modules


urlpatterns = [Path('', modules.login, name='home')]