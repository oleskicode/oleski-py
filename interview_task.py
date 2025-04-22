# You are given an array of objects representing test cases.
# Your task is to write a function that processes this array to generate a summary object.
# The summary should count the number of test cases for each status and group all test descriptions by their status.
# Input Example:
testCases = [
    { "id": 1, "description": "Login with valid credentials", "status": "passed" },
    { "id": 2, "description": "Login with invalid credentials", "status": "failed" },
    { "id": 3, "description": "Forgot password flow", "status": "skipped" },
    { "id": 4, "description": "Update profile", "status": "passed" },
    { "id": 5, "description": "Delete account", "status": "failed" },
]

# Output Example:
# {
#     passed: {
#         count: 2,
#         descriptions: ["Login with valid credentials", "Update profile"]
#     },
#     failed: {
#         count: 2,
#         descriptions: ["Login with invalid credentials", "Delete account"]
#     },
#     skipped: {
#         count: 1,
#         descriptions: ["Forgot password flow"]
#     }
# }

import json

def generate_summary(input_list: list) -> json:
    print(input_list)
    summary_dict = {"passed":{},"failed":{},"skipped":{}}
    passed_list = []
    failed_list = []
    skipped_list = []
    for item in input_list:
        if item["status"] == "passed":
            passed_list.append(item["description"])
        if item["status"] == "failed":
            failed_list.append(item["description"])
        if item["status"] == "skipped":
            skipped_list.append(item["description"])
    summary_dict["passed"]["count"] = len(passed_list)
    summary_dict["failed"]["count"] = len(failed_list)
    summary_dict["skipped"]["count"] = len(skipped_list)
    summary_dict["passed"]["descriptions"] = passed_list
    summary_dict["failed"]["descriptions"] = failed_list
    summary_dict["skipped"]["descriptions"] = skipped_list
    return json.dumps(summary_dict)


print(generate_summary(testCases))
