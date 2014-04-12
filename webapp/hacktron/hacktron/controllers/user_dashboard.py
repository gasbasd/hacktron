from tg import expose
from hacktron.lib.base import BaseController


class UserDashboardController(BaseController):
    @expose()
    def index(self, **kw):
        user_info = {'name': 'Pippo',
                     'surname': 'Disney',
                     'car_model': 'E-Tron'
                    }
        return {'user_info':user_info}