import cv2

v = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('a.avi',fourcc,30,(640,480))
while 1:
    c,f = v.read()
    f = cv2.flip(f,1)
    out.write(f)
    cv2.imshow('1',f)

    if cv2.waitKey(1) == ord('q'):
        break

v.release()
out.release()
cv2.destroyAllWindows()
