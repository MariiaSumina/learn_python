# ------------------------------------------------------------
# Global variables
# ------------------------------------------------------------
theDetails = []
theSize = 0

# ------------------------------------------------------------
# Subprograms
# ------------------------------------------------------------
def getImageDetails ():
    width = 0
    height = 0
    colours = 0
    details = []

    # Get input from the user
    width = int (input ("Enter image width in pixels: "))
    height = int (input ("Enter image height in pixels: "))
    colours = int (input ("Enter colour depth in bits: "))

    # Build a list of data to return the caller
    details.append (width)
    details.append (height)
    details.append (colours)

    return (details)

def calculateImageSize (pWidth, pHeight, pColourDepth):
    size = 0

    # Calculate the size in bits
    size = pWidth * pHeight * pColourDepth

    return (size)

def outputToUser (pImageSize):
    print ("Your image is " + str (pImageSize) + " bits")

def covertSize(pFileSize):
    kib = pFileSize / (8*1024)
    mib = pFileSize/(8*1024*1024)
    print(f"This is the same as {kib} KiB and {mib} MiB")

# ------------------------------------------------------------
# Main program
# ------------------------------------------------------------
theDetails = getImageDetails ()
theSize = calculateImageSize (theDetails[0], theDetails[1], theDetails[2])
outputToUser (theSize)
covertSize(theSize)
