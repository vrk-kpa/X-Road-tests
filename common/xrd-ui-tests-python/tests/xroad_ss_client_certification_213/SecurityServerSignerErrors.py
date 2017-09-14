import unittest

from main.maincontroller import MainController
from tests.xroad_ss_client_certification_213 import client_certification_2_1_3


class SecurityServerKeyGenerationSignerTimedOut(unittest.TestCase):
    def test_securityServerSignerTimedOut(self):
        main = MainController(self)
        ss_host = main.config.get('ss2.host')
        ss_username = main.config.get('ss2.user')
        ss_pass = main.config.get('ss2.pass')
        ss2_ssh_host = main.config.get('ss2.ssh_host')
        ss2_ssh_user = main.config.get('ss2.ssh_user')
        ss2_ssh_pass = main.config.get('ss2.ssh_pass')

        generate_key_timed_out = client_certification_2_1_3.test_generate_key_timed_out(main,
                                                                                        ss_host,
                                                                                        ss_username,
                                                                                        ss_pass,
                                                                                        ss2_ssh_host,
                                                                                        ss2_ssh_user,
                                                                                        ss2_ssh_pass)

        start_xroad_signer_service = client_certification_2_1_3.start_xroad_signer_service(main,
                                                                                           ss2_ssh_host,
                                                                                           ss2_ssh_user,
                                                                                           ss2_ssh_pass)
        '''SS_28 5a key generation fails when token service is unavailable'''
        main.log('SS_28 5a key generation fails when token service is unavailable')
        try:
            generate_key_timed_out()
        except:
            assert False
        finally:
            start_xroad_signer_service()
            main.tearDown()


class SecurityServerCSRGeneration(unittest.TestCase):
    def test_securityServerCSRGenerationSignerTimedOut(self):
        main = MainController(self)
        ss_host = main.config.get('ss2.host')
        ss_username = main.config.get('ss2.user')
        ss_pass = main.config.get('ss2.pass')
        ss2_ssh_host = main.config.get('ss2.ssh_host')
        ss2_ssh_user = main.config.get('ss2.ssh_user')
        ss2_ssh_pass = main.config.get('ss2.ssh_pass')

        generate_csr_timed_out = client_certification_2_1_3.test_generate_csr_timed_out(main,
                                                                                        ss_host,
                                                                                        ss_username,
                                                                                        ss_pass,
                                                                                        ss2_ssh_host,
                                                                                        ss2_ssh_user,
                                                                                        ss2_ssh_pass)

        start_xroad_signer_service = client_certification_2_1_3.start_xroad_signer_service(main,
                                                                                           ss2_ssh_host,
                                                                                           ss2_ssh_user,
                                                                                           ss2_ssh_pass)
        '''SS_29 6a csr generation fails when token service is unavailable'''
        main.log('SS_29 6a csr generation fails when token service is unavailable')
        try:
            generate_csr_timed_out()
        except:
            assert False
        finally:
            start_xroad_signer_service()
            client_certification_2_1_3.delete_added_key_after_service_up(main, ss_host)
            main.tearDown()
