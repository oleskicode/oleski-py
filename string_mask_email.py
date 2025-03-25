def mask_email(email: str) -> str:
    """Function which masks email address."""
    # print(email.find("@")) # index of @
    domain = "@" + email.split(sep="@")[1]
    return email[0] + "***" + email[email.find("@") - 1] + domain


print(mask_email.__doc__)
print(mask_email("robin@example.com"))  # "r***d@example.com"
