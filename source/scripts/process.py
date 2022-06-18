from compress import compress_asset
from whitespace import remove_whitespaces
from realign import realign_asset
import cv2
import numpy as np

def process_asset(filename,outputfilename,refFilename=None,compress=True,trim=True,realign=False,debug=True):
    print("INFO: STARTING OPTIMIZATION")
    if compress:
        print("INFO: STARTING COMPRESSION")
        compress_asset(filename,outputfilename)
    if trim:
        print("INFO: STARTING WHITESPACE REDUCTION AND CORRECTION")
        remove_whitespaces(filename,outputfilename)
    if realign:
        print("INFO: STARTING ALIGNMENT CORRECTION")
        realign_asset(outputfilename,outputfilename,refFilename)

        
    if "pdf" not in filename.lower() and debug:
        template = cv2.imread(filename)
        image = cv2.imread(outputfilename)
        
        h1, w1 = template.shape[:2]
        h2, w2 = image.shape[:2]


        #create empty matrix
        vis = np.zeros((max(h1, h2), w1+w2,3), np.uint8)

        #combine 2 images
        vis[:h1, :w1,:3] = template
        vis[:h2, w1:w1+w2,:3] = image
        
        # show the two output image alignment visualizations
        cv2.imshow("Image Processed", vis)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
        
    print("INFO: PROCESS COMPLETED!")


if __name__ == "__main__":
    filename = "../sample_data/pan.jpeg"
    outputfilename = "../sample_data/pan_processed.jpeg"

    # filename = "../sample_data/sbi-statement.jpeg"
    # outputfilename = "../sample_data/sbi-statement-processed.jpeg"

    # filename = "../sample_data/link-aadhaar.pdf"
    # outputfilename = "../sample_data/link-aadhaar-processed.pdf"

    # filename = "../sample_data/IBRegForm.pdf"
    # outputfilename = "../sample_data/IBRegForm-processed.pdf"

    process_asset(filename,outputfilename)

    # filename = "../sample_data/Form-60-rotated.jpeg"
    # outputfilename = "../sample_data/Form-60-processed.jpeg"
    # reffilename = "../sample_data/Form-60.jpeg"
    # process_asset(filename,outputfilename,reffilename,realign=True)