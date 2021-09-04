import os


def filetree(root, path="", exep=[".py", ".md"]):

    # Stop if this is not a folder:
    if not os.path.isdir(root):
        return

    # Get files in current folder:
    files = sorted(os.listdir(root))

    # Filter files based on exep
    files_filtered = [item for item in files if (not item.startswith(".") and
                                                 not os.path.splitext(item)[1] in exep)]

    # Split filtered files into separate file and directory lists
    files = []
    directories = []
    for f in files_filtered:
        if os.path.isdir(f"{root}/{f}"):
            directories.append(f)
        else:
            files.append(f)

    # Store length for easier access
    nfiles = len(files)
    ndirs = len(directories)

    # Print all the files of current directory first
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(nfiles):
        if i == nfiles - 1 and ndirs == 0:
            newpath = path + "    "
            arrow = "-- "
        print(f"{path}{arrow}{files[i]}")

    # Print the content of sub-folders recursively
    newpath = path + "|   "
    arrow = "|-- "
    for i in range(ndirs):
        if i == ndirs - 1:
            newpath = path + "    "
            arrow = "-- "
        print(f"{path}{arrow}{directories[i]}")
        filetree(f"{root}/{directories[i]}", newpath, exep)


def main():
    print("The contents of the current folder are:")
    print("--" * 8)
    filetree(".")
    print("--" * 8)


if __name__ == "__main__":
    main()
