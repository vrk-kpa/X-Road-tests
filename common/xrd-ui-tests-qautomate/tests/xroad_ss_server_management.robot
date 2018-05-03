*** Settings ***

Suite Setup     Test suite setup
Suite Teardown  Test suite teardown
Test Setup      setup
Test Teardown   teardown

Library     libraries.QautoRobot  ${TESTDATA}


*** Variables ***
${ss1_url}=  ss1_url
${security_server_url_wrong_password}=  security_server_url_wrong_password

${login_user}=  Log in user
${logout_user}=  Log out user
${login_user_failed}=  Log in user failed
${login_restore_in_progress}=  Restore in progress, try again later
${authentication_failed}=  Authentication failed

${backup_directory}=  /var/lib/xroad/backup
${lanquage_eng}=  ENGLISH (EN)
${set_ui_language}=  Set UI language

${True}=  True
${False}=  False

*** Test Cases ***
Test login and logout ss gui
    # Step Open security server for login add user name password
    # Step System verify's login success and log file
    Ss login  ${ss1_url}

    # Step System logs the event "Log in user" to the audit log
    Ssh verify audit log  ${ss1_url}  ${login_user}

    # Step Log out from system GUI
    Log_out

    # Step System logs the event “Log out user” to the audit log.
    Ssh verify audit log  ${ss1_url}  ${logout_user}

Test login with wrong password
    # Step Open security server The user with the inserted user name does not exist or the password is incorrect.
    Ss login  ${security_server_url_wrong_password}  initial_conf=${True}  wait_for_jquery=${False}

    # Step System displays the error message “Authentication failed”.
    Ss verify login fail  ${authentication_failed}
    Ssh verify audit log  ${ss1_url}  ${login_user_failed}

Test login restore back up in process
    Open browser
    Ss login  ${ss1_url}
    Ss sidebar open backup restore view
    Ss backup generate backup
    Ss backup restore click element first row restore
    Ss backup restore confirm restore click button confirm  ${False}

    Switch browser  ${AutogenBrowser}
    # Step Open security server for login add user name password
    Ss login  ${ss1_url}  initial_conf=${True}  wait_for_jquery=${False}

    # The system is currently undergoing the system restore process.
    # 3a.1. System displays the error message “Restore in progress, try again later”.
    Ss verify login fail  ${login_restore_in_progress}
    # 3a.2. System logs the event “Log out user” to the audit log.
    Ssh verify audit log  ${ss1_url}  ${logout_user}

Test change language
    # Step Open security server for login add user name password
    Ss login  ${ss1_url}

    # Step Change language
    Common open select language_dlg
    Common change language in dlg  ${lanquage_eng}
    Common accept select language dlg

    # Step Verify audit log for language change
    Ssh verify audit log  ss1_url  ${set_ui_language}


*** Keywords ***
setup
    Start recording  ${TEST NAME}

    Empty all logs from server  ${ss1_url}

teardown
    ${failure_image_path}=  Get failure image path  ${TEST NAME}
    Run Keyword If Test Failed  Take full screenshot  ${failure_image_path}
    Run Keyword If Test Failed  Set Suite Metadata  ${TEST NAME} failure  file:///${failure_image_path}

    # Step log out if logged in
    ${verify_login_page}=  Ss login verify is login page
    Run Keyword If  "${verify_login_page}"=="${False}"  Log out

    ${recording_path}=  Stop recording
    Run Keyword If Test Failed  Set Suite Metadata  ${TEST NAME} recording  file:///${recording_path}

Test suite setup
    ${AutogenBrowser}=  Open browser  ${BROWSER}
    Set suite variable  ${AutogenBrowser}  ${AutogenBrowser}

Test suite teardown
    Close all browsers
    Ssh delete files from directory  ${ss1_url}  ${backup_directory}
