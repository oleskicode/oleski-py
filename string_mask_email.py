# Function which masks email address
# Test Data : print(mask_email("robin_hood@example.com")) # "r***d@example.com"


def mask_email(email: str) -> str:
    # print(email.find("@")) # index of @
    domain = "@" + email.split(sep="@")[1]
    return email[0] + "***" + email[email.find("@") - 1] + domain


print(mask_email("robin@example.com"))
