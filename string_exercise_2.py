# function which masks email address
# Test Data : print(mask_email("robin_hood@example.com")) # "r***d@example.com"

def mask_email(email: str) -> str:
    # print(email.find("@")) # index of @
    domain = "@" + email.split(sep="@")[1]
    output_string = email[0] + "***" + email[email.find("@")-1] + domain
    return output_string

print(mask_email("robin@example.com"))