from zope.interface import implements
from zope.component import getMultiAdapter
from AccessControl import getSecurityManager
from zope.viewlet.interfaces import IViewlet
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from Acquisition import aq_inner
from Products.CMFCore.utils import getToolByName
from big.brother.model import session, model
from sqlalchemy import desc
import datetime


class UserViewsViewlet(BrowserView):
    """
    A "hidden" viewlet which records when a user views and object. I know, 
    this does seem a bit hacky. In the future maybe an event will do but I'm
    not sure what event will work (IBeforeTraverseEvent or IEndRequestEvent?) 
    and short on time for this one.
    """
    implements(IViewlet)
    render = ViewPageTemplateFile('templates/user_viewed.pt')

    def __init__(self, context, request, view=None, manager=None):
        super(UserViewsViewlet, self).__init__(context, request)
        self.__parent__ = view
        self.view = view
        self.manager = manager
        self.portal_state = getMultiAdapter((context, self.request), 
                                            name=u"plone_portal_state")
        self.context = context
        self.anonymous = self.portal_state.anonymous()
        self._markViewed()
        
        
    def _markViewed(self):
        """
        Log that the current user has viewed this item
        """
        if self.anonymous:
            return False
        
        sqlSession = session.SQL_SESSION()
        userId = self.portal_state.member().getId()
        
        record = model.UserView(username=userId, uid=self.context.UID(),
                                date = datetime.datetime.now(),
                                url = self.context.absolute_url_path()
                                )
        sqlSession.add(record)
        sqlSession.commit()
        sqlSession.close()
        
        return True

    


                 




