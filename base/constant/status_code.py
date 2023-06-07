from rest_framework import status

############STATUS###############

ok = status.HTTP_200_OK
not_found = status.HTTP_404_NOT_FOUND
bad_request = status.HTTP_400_BAD_REQUEST
created = status.HTTP_201_CREATED
no_content = status.HTTP_204_NO_CONTENT

############ERRORS######################
data_exists = ['the data currently exists']
field_required_error = ['This field is required']
does_not_exist = ["Does not exist"]

###############SUCCESS##################
updated = ['Success Updating']
register_success = ['Successfully Registered']
login_success = ['Successfully Login']
incorrect_value = ['Incorrect input']


#################VALIDATION###################

username_exist = 'Username already exist!'
email_exist = 'Email already exist!'
password_not_match = "Password doesn't match!"
login_fail = 'Invalid Username or Password'