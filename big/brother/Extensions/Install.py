from cStringIO import StringIO
from Products.CMFCore.utils import getToolByName


def runProfile(portal, profileName):
    setupTool = getToolByName(portal, 'portal_setup')
    setupTool.runAllImportStepsFromProfile(profileName)

def install(portal):
    """Run the GS profile to install this package"""
    out = StringIO()
    runProfile(portal, 'profile-big.brother:default')
    print >>out, "Installed big.brother"
    return out.getvalue()

def uninstall(portal, reinstall=False):
    """Run the GS profile to install this package"""
    out = StringIO()
    if not reinstall:
        runProfile(portal, 'profile-big.brother:uninstall')
        print >>out, "Uninstalled big.brother"
    return out.getvalue()