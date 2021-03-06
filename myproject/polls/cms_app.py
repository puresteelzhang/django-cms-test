from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.utils.translation import ugettext_lazy as _

from polls.menu import PollsMenu

class PollsApps(CMSApp):
    name = _("Poll Apps") # give your app a name, this is required
    urls = ["polls.urls"] # link your app to url configuration(s)
    menus = [PollsMenu] # attach a CMSAttachMenu to this apphook.

apphook_pool.register(PollsApps) # register your app