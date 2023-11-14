*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  kallee
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Succeed

Register With Too Short Username And Valid Password
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Invalid username: Username must be at least three characters long

Register With Valid Username And Invalid Password
# salasana ei sisällä halutunlaisia merkkejä
    Set Username  kalleeee
    Set Password  kalleeee
    Set Password Confirmation  kalleeee
    Submit Credentials
    Registration Should Fail With Message  Invalid password: Password cannot consist only of letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kalleee
    Set Password  kalleee123
    Set Password Confirmation  kallee123
    Submit Credentials
    Registration Should Fail With Message  Password confirmation does not match password

Login After Successful Registration
    Go To Login Page
    Set Username  jaakko
    Set Password  jaakko123
    Click Login
    Login Should Succeed

Login After Failed Registration
    Set Username  k
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Registration Should Fail With Message  Invalid username: Username must be at least three characters long
    Go To Login Page
    Set Username  k
    Set Password  kalle123
    Click Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Registration Should Succeed
    Welcome Page Should Be Open

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${passwordconfirmation}
    Input Password  password_confirmation  ${passwordconfirmation}

Submit Credentials
    Click Button  Register

Registration Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Create User And Go To Register Page
    Create User  jaakko  jaakko123
    Go To Register Page
    Register Page Should Be Open

Click Login
    Click Button  Login

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}