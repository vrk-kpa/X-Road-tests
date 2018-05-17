from __future__ import absolute_import

import unittest

from helpers import xroad, auditchecker
from main.maincontroller import MainController
from tests.xroad_ss_client_certification_213 import client_certification


class XroadSecurityServerClientKeyDeletion(unittest.TestCase):
    """
    SS_36 Delete a Key from a Software Token
    RIA URL: https://jira.ria.ee/browse/XT-348, https://jira.ria.ee/browse/XTKB-88, https://jira.ria.ee/browse/XTKB-32
    Depends on finishing other test(s): MEMBER_53
    Requires helper scenarios:
    X-Road version: 6.16.0
    """
    def __init__(self, methodName='test_security_server_key_deletion'):
        unittest.TestCase.__init__(self, methodName)

    def test_security_server_key_deletion(self):
        # Instantiate MainController
        main = MainController(self)

        # Set test name and number
        main.test_number = 'SS_36'
        main.test_name = self.__class__.__name__

        main.url = main.config.get('ss2.host')
        main.username = main.config.get('ss2.user')
        main.password = main.config.get('ss2.pass')
        ss1_host = main.config.get('ss1.host')
        ss1_user = main.config.get('ss1.user')
        ss1_pass = main.config.get('ss1.pass')
        ss2_ssh_host = main.config.get('ss2.ssh_host')
        ss2_ssh_user = main.config.get('ss2.ssh_user')
        ss2_ssh_pass = main.config.get('ss2.ssh_pass')

        ss1_client = xroad.split_xroad_id(main.config.get('ss1.client_id'))
        ss1_client_2 = xroad.split_xroad_id(main.config.get('ss1.client2_id'))

        ss2_client = xroad.split_xroad_id(main.config.get('ss2.client_id'))

        main.log('Deleting certificate')

        try:
            # Create webdriver and go to main URL
            main.reset_webdriver(main.url, main.username, main.password)
            # Delete the key
            log_checker = auditchecker.AuditChecker(ss2_ssh_host, ss2_ssh_user, ss2_ssh_pass)
            client_certification.delete_added_key(main, ss2_client, cancel_deletion=True, log_checker=log_checker)
            main.reload_webdriver(ss1_host, ss1_user, ss1_pass)
            client_certification.delete_added_key(main, ss1_client)
            client_certification.delete_added_key(main, ss1_client_2)
        except:
            main.log('Failed to delete certificate.')
            main.save_exception_data()
            raise
        finally:
            main.tearDown()
