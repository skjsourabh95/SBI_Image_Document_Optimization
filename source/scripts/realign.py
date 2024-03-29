import cv2
import imutils
import numpy as np

# NEED A REFERNCE IMAGE TO ALIGN USING KEY POINTS FEATURES

def align_images(image, template, maxFeatures=500, keepPercent=0.2,debug=False):
    # convert both the input image and template to grayscale
    imageGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    # use ORB to detect keypoints and extract (binary) local
    # invariant features
    orb = cv2.ORB_create(maxFeatures)
    (kpsA, descsA) = orb.detectAndCompute(imageGray, None)
    (kpsB, descsB) = orb.detectAndCompute(templateGray, None)
    # match the features
    method = cv2.DESCRIPTOR_MATCHER_BRUTEFORCE_HAMMING
    matcher = cv2.DescriptorMatcher_create(method)
    matches = matcher.match(descsA, descsB, None)
    # sort the matches by their distance (the smaller the distance,
    # the "more similar" the features are)
    matches = sorted(matches, key=lambda x:x.distance)
    # keep only the top matches
    keep = int(len(matches) * keepPercent)
    matches = matches[:keep]
    # check to see if we should visualize the matched keypoints
    if debug:
        matchedVis = cv2.drawMatches(image, kpsA, template, kpsB,matches, None)
        matchedVis = imutils.resize(matchedVis, width=1000)
        cv2.imshow("Matched Keypoints", matchedVis)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    # allocate memory for the keypoints (x, y)-coordinates from the
    # top matches -- we'll use these coordinates to compute our
    # homography matrix
    ptsA = np.zeros((len(matches), 2), dtype="float")
    ptsB = np.zeros((len(matches), 2), dtype="float")
    # loop over the top matches
    for (i, m) in enumerate(matches):
        # indicate that the two keypoints in the respective images
        # map to each other
        ptsA[i] = kpsA[m.queryIdx].pt
        ptsB[i] = kpsB[m.trainIdx].pt
    # compute the homography matrix between the two sets of matched
    # points
    (H, mask) = cv2.findHomography(ptsA, ptsB, method=cv2.RANSAC)
    # use the homography matrix to align the images
    (h, w) = template.shape[:2]
    aligned = cv2.warpPerspective(image, H, (w, h))
    # return the aligned image
    return aligned

def realign_asset(imFilename,outfilename,refFilename,debug=False):
    if "pdf" in imFilename:
        print("ERROR : PLEASE PROVIDE AN IMAGE!")
        return
    if not refFilename:
        print("ERROR : PLEASE PROVIDE A REFERENCE IMAGE!")
        return
    if not outfilename:
        print("ERROR : PLEASE PROVIDE A OUTPUT IMAGE PATH!")
        return
    
    template = cv2.imread(refFilename)
    image = cv2.imread(imFilename)
    aligned = align_images(image, template, debug=True)

    stacked = np.hstack([aligned, template])
    
    if debug:
        # show the two output image alignment visualizations
        cv2.imshow("Image Alignment Stacked", stacked)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    cv2.imwrite(outfilename,aligned)

if __name__ == '__main__':
    # Read reference image
    refFilename = "../sample_data/Form-60.jpeg"
    imFilename = "../sample_data/Form-60-rotated.jpeg"

    template = cv2.imread(refFilename)
    image = cv2.imread(imFilename)
    aligned = align_images(image, template, debug=True)

    stacked = np.hstack([aligned, template])
    # show the two output image alignment visualizations
    cv2.imshow("Image Alignment Stacked", stacked)
    cv2.waitKey(0)
    cv2.destroyAllWindows()