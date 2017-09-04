# -*- coding: utf-8 -*-
from selenium.webdriver.common.by import By
from webframework.extension.util.common_utils import *
from time import sleep
from common_lib import Common_lib
from pagemodel.cs_login import Cs_login
from pagemodel.open_application import Open_application
from pagemodel.cs_sidebar import Cs_sidebar

class Component_cs(CommonUtils):
    """
    Common components to central server

    Changelog:

    * 11.07.2017
        | Documentation updated
    """
    common_lib = Common_lib()
    cs_login = Cs_login()
    open_application = Open_application()
    cs_sidebar = Cs_sidebar()

    def __init__(self, parameters=None):
        """
        Initilization method for moving test data to class

        *Updated: 11.07.2017*

        :param parameters:  Test data section dictionary
        """
        CommonUtils.__init__(self)
        self.parameters = parameters

    def login(self, section=u'cs_static_url', initial_conf=False):
        """
        Login to central server

        *Updated: 11.07.2017*

        :param section:  Test data section name
        :param initial_conf:  If true server is in configurations state
        
        **Test steps:**
                * **Step 1:** :func:`~pagemodel.open_application.Open_application.open_application_url`, *self.parameters[section]*
                * **Step 2:** :func:`~pagemodel.cs_login.Cs_login.login_dev_cs`, *self.parameters[section]*
                * **Step 3:** :func:`~pagemodel.cs_sidebar.Cs_sidebar.verify_central_server_title`
        """
        ## Login
        self.open_application.open_application_url(self.parameters[section])
        self.cs_login.login_dev_cs(self.parameters[section])
        if not initial_conf:
            self.cs_sidebar.verify_central_server_title()

    def open_central_server_url(self, section=u'cs_static_url'):
        """
        Open central server url

        *Updated: 11.07.2017*
        
        :param section:  Test data section name
        
        **Test steps:**
                * **Step 1:** :func:`~pagemodel.open_application.Open_application.open_application_url`, *self.parameters[section]*
        """
        self.open_application.open_application_url(self.parameters[section])