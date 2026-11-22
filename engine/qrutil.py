import cv2, numpy as np
def load(im):
    return cv2.imdecode(np.frombuffer(im.data, np.uint8), cv2.IMREAD_GRAYSCALE)
def is_qr_candidate(arr):
    return arr is not None and min(arr.shape) >= 50 and abs(arr.shape[0] - arr.shape[1]) <= 4
def qdec(arr):
    det = cv2.QRCodeDetector()
    d, _, _ = det.detectAndDecode(arr)
    if d: return d
    for k in (2, 3, 4, 5):
        b = cv2.copyMakeBorder(cv2.resize(arr, None, fx=k, fy=k, interpolation=cv2.INTER_NEAREST), 40, 40, 40, 40, cv2.BORDER_CONSTANT, value=255)
        d, _, _ = det.detectAndDecode(b)
        if d: return d
    return ""
