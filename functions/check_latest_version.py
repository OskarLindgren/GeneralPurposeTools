import urllib.request

def CheckVersion(version=None):
    # Check if version was passed
    if version == None: 
        print("Version not found")
        input("Enter to continue...")
        return

    try: # will fail if the pc doesn't have an internet connection
        with urllib.request.urlopen(url='https://api.github.com/repos/OskarLindgren/GeneralPurposeTools/releases/latest', timeout=0.5) as response:
            body = str(response.read())
            # get the "tag_name" portion
            body = body.split(",")
            for item in body:
                if "tag_name" in item:
                    tag = item
    except Exception:
        print("Unable to check for latest version, check your internet connection!")
        input("Enter to continue...")
        return

    # Check if the current version matches with the tag on github
    if version not in tag:
        print("Your not on the latest version!")
        print("You can get the latest version on github:")
        print("https://github.com/OskarLindgren/GeneralPurposeTools/releases/latest")
        input("Enter to continue...")
        return

    # If everything is fine, just return nothing
    return

if __name__ == '__main__':
    CheckVersion()
