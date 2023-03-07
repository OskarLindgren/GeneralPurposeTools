import os
import win32api

def displayDir(dir: str=None, mode: str=None, outdir: str=None):
    os.system("Title GPT - Display Dir")

    ### OPTIONS

    # fix dir
    if dir == None:
        while True:
            dir = input("Please enter the path to the directory you want to display:\n")
            if os.path.isdir(dir):
                break

            print("That's not a valid directory")
            input("...")
            os.system("cls")

    # fix outdir
    if outdir == None:
        outdir = f"{os.path.expanduser('~')}\\Desktop"
        # if that's not a valid path then the user is likely using OneDrive for their desktop
        if not os.path.isdir(outdir):
            outdir = f"{os.path.expanduser('~')}\\OneDrive\\Desktop"
            # if it's still not a valid path, admin defeat and place it in "C:\\GPToutput"
            if not os.path.isdir(outdir):
                outdir = "C:\\GPToutput"
                os.mkdir(outdir)
                print(f"Could not find desktop path. Placing output in {outdir}")

    if ":" not in outdir:
        print("Output directory must be an absolute path")
        input("...")
        return
    
    if not os.path.exists(outdir):
        print("Output directory doesn't exist")
        input("...")
        return

    # fix mode
    if mode == None:
        while True:
            print("You did not specify a mode, please select one below:\n1) Show only folders\n2) Show folders and files\n3) Show folders, files and hidden files")
            choice = int(input())

            try:
                int(choice)
            except ValueError:
                continue

            # 1, 2, 3
            if 0 < choice < 4:
                mode = choice
                break
            
            print("That's not an option")
            input("...")
            os.system("cls")

    elif type(mode) == str:
        if mode.isdigit():
            if 0 < int(mode) < 4:
                mode = int(mode)
            else:
                print("You selected a mode that is not an option!")
                input("...")
                return
        else:
            if "folders" in mode.lower():
                mode = 1
            elif "files" in mode.lower():
                mode = 2
            elif "hidden" in mode.lower():
                mode = 3
            else:
                print("You selected a mode that is not an option!")
                input("...")
                return
            
    else:
        # 1, 2, 3
        if 0 < choice < 4:
            mode = choice
        else:
            print("You selected a mode that is not an option!")
            input("...")
            return
            

    ### FIND FILES
    os.system("cls")
    print("Working...")

    output = open(f"{outdir}{os.sep}FolderStructure.txt", "a", encoding="utf-8")

    if mode == 1:
        for root, _, _ in os.walk(dir):
            lvl = root.replace(dir, '').count(os.sep) # how deep we are in the tree
            indent = '| ' * lvl
            output.write(f"{indent}📂 {os.path.basename(root)}\n")

    elif mode == 2:
        for root, _, files in os.walk(dir):
            lvl = root.replace(dir, '').count(os.sep) # how deep we are in the tree
            indent = ' ' * 2 * lvl
            sub_indent = ' ' * 2 * (lvl+1)
            output.write(f"{indent}{'└📂 ' if lvl == 0 else ' 📂 '}{os.path.basename(root)}/\n")
            for f in files:
                # check if the file is hidden
                try:
                    if not win32api.GetFileAttributes(f"{root}{os.sep}{f}") & 2:
                        output.write(f"{sub_indent}{'└📄 ' if f == files[-1] else '├📄 '}{f}\n") # last file in a dir will give └
                except Exception:
                    output.write(f"{sub_indent}{'└📄 ' if f == files[-1] else '├📄 '}{f} (open in another process)\n") # last file in a dir will give └

    else:
        for root, _, files in os.walk(dir):
            lvl = root.replace(dir, '').count(os.sep) # how deep we are in the tree
            indent = ' ' * 2 * lvl
            sub_indent = ' ' * 2 * (lvl+1)
            output.write(f"{indent}{'└📂 ' if lvl == 0 else ' 📂 '}{os.path.basename(root)}/\n")
            for f in files:
                # check if the file is hidden
                try:
                    if win32api.GetFileAttributes(f"{root}{os.sep}{f}") & 2:
                        output.write(f"{sub_indent}{'└📄 ' if f == files[-1] else '├📄 '}{f} (hidden)\n") # last file in a dir will give └
                    else:
                        output.write(f"{sub_indent}{'└📄 ' if f == files[-1] else '├📄 '}{f}\n") # last file in a dir will give └
                except Exception:
                    output.write(f"{sub_indent}{'└📄 ' if f == files[-1] else '├📄 '}{f} (open in another process)\n") # last file in a dir will give └

    output.close()
    os.system("cls")
    print("\"(open in another process)\", implies that a check for hidden status failed.")
    print("Done!")
    input("...")
    return

if __name__ == "__main__":
    displayDir("C:\\Users\\oskar\\Desktop\\dirtest")