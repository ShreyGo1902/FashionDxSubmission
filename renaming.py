import os


# Function to rename the files
# Run this program 3 times (1 each for stripes, solids and checks)
def main():
    i = 0

    for filename in os.listdir("/home/shreyas/Training Set/stripes"):
        dst = "Stripes." + str(i) + ".jpg"
        src = '/home/shreyas/Training Set/stripes/' + filename
        dst = '/home/shreyas/Training Set/stripes/' + dst

        # rename() function will
        # rename all the files
        os.rename(src, dst)
        i += 1


if __name__ == '__main__':
    main()
