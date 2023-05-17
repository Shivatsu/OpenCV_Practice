import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
print(cap.isOpened())
while True:
    ret, frame = cap.read()

    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))   # 4 = Height Prop ID
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))    # 3 = Width Prop ID
        print(cap.get(5))  # 5 = FPS Prop ID or CAP_PROP_FPS

        out.write(frame)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
