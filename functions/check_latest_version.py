import urllib.request

def CheckVersion(version=None):
    ### Check if the pc has an internet connection (it needs one to check if it's on the latest version)
    try:
        urllib.request.urlopen(url='https://www.google.com/', timeout=1)
    except Exception:
        print("Unable to check for latest version, check your internet connection!")
        input("Enter to continue...")
        return

    ### Check that version was passed
    if version == None: 
        print("Version not found")
        input("Enter to continue...")
        return
    
    ### Check what the latest version on github
    with urllib.request.urlopen(url='https://api.github.com/repos/OskarLindgren/GeneralPurposeTools/releases/latest', timeout=1) as response:
        body = str(response.read())
        # get the "tag_name" portion
        body = body.split(",")
        for item in body:
            if "tag_name" in item:
                tag = item

    ### Check if the current version matches with the tag on github
    if version not in tag:
        print("Your not on the latest version!")
        print("You can get the latest version on github:")
        print("https://github.com/OskarLindgren/GeneralPurposeTools/releases/latest")
        input("Enter to continue...")
        return

    ### If everything is fine, just return nothing
    return

    

if __name__ == '__main__':
    CheckVersion()
