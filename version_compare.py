def version_compare(version1: str, version2: str) -> str:
    """Compare version and return the newer one"""
    list1 = version1.split(".")
    list2 = version2.split(".")

    # normalize lists size by adding zeros
    max_len = max(len(list1), len(list2))
    list1.extend(["0"] * (max_len - len(list1)))
    list2.extend(["0"] * (max_len - len(list2)))
    print(list1)
    print(list2)

    for i in range(len(list1)):
        if list1[i] == list2[i]:
            continue
        if list1[i] > list2[i]:
            return version1
        else:
            return version2

    return version1 # if identical

print(version_compare.__doc__)

build_vers1 = "126.17.18.1"
build_vers2 = "126.17"
print(version_compare(build_vers1, build_vers2))

build_vers3 = "126.15.16.33"
build_vers4 = "126.17.18.4"
print(version_compare(build_vers3, build_vers4))

build_vers5 = "126.15.16.55"
build_vers6 = "126.17.6"
print(version_compare(build_vers5, build_vers6))

build_vers7 = "126.0.5"
build_vers8 = "126.0.2.7"
print(version_compare(build_vers7, build_vers8))
