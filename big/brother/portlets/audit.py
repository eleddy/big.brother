from zope import schema
from zope.interface import implements
from zope.formlib import form
from zope.component import getMultiAdapter
from zope.security import checkPermission
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.portlets.interfaces import IPortletDataProvider
from plone.app.portlets.portlets import base
from plone.app.vocabularies.catalog import SearchableTextSourceBinder
from big.brother.model import session, model
from sqlalchemy import desc
import datetime
from Products.CMFCore.interfaces import IContentish


class IAuditPortlet(IPortletDataProvider):
    """This portlet takes the userviews view and displays it in a portlet
    """
    portletTitle = schema.TextLine(
        title = u"Portlet title",
        description = u"The title of the portlet.",
        required = True,
        default = u"Audit Trail"
        )


class Assignment(base.Assignment):
    implements(IAuditPortlet)

    def __init__(self, portletTitle=u"Audit Trail"):
        self.portletTitle = portletTitle
        
    @property    
    def title(self):
        return self.portletTitle

class Renderer(base.Renderer):
    render = ViewPageTemplateFile('templates/audit.pt')
    
    def __init__(self, context, request, view, manager, data):
        super(Renderer, self).__init__(context, request, view, manager, data)       
        self.portal_state = getMultiAdapter((context, self.request), 
                             name=u"plone_portal_state")
        self.portletTitle = data.portletTitle
        self.anonymous = self.portal_state.anonymous()
        self.context = context
        

        
    def getAuditLog(self):
        """
        Return a list of usernames of people that have viewed an 
        item, along with the time they viewed it and that members 
        full name.
        """
        results = []
        uid = self.context.UID()
        sqlSession = session.SQL_SESSION()
        q = sqlSession.query(model.UserView).filter(model.UserView.uid==uid)
        for userview in q.group_by(model.UserView.username).order_by(desc(model.UserView.date)):
            results.append({'username': userview.username, 
                            'date': userview.date,
                            'name': self.getMemberName(userview.username),
                            })
            
        return results
        
    def getMemberName(self, member_id):
        """Given a member_id, return the registered name"""
        mtool = getToolByName(self.context, 'portal_membership')
        member = mtool.getMemberById(member_id)
        if member:
            return member.getProperty('fullname','') or member_id
        return member_id
            
    
    
    @property
    def available(self):
        if self.anonymous:
            return False
            
        if not IContentish.providedBy(self.context):
            return False 
            
        return checkPermission('big.brother.ViewAuditLog', self.context)


        
class AddForm(base.AddForm):
    form_fields = form.Fields(IAuditPortlet)

    def create(self, data):
        return Assignment(**data)

class EditForm(base.EditForm):
    form_fields = form.Fields(IAuditPortlet)
