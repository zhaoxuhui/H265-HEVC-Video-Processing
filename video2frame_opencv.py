import cv2

if __name__ == '__main__':
    video_path = "./D01_20201011131153.mp4"
    out_path = "./frames"
    out_type = ".jpg"
    time_interval = 50

    cap = cv2.VideoCapture(video_path)
    frames = int(cap.get(7))
    fps = int(cap.get(5))
    video_width = int(cap.get(3))
    video_height = int(cap.get(4))
    frame_interval = time_interval * fps

    total_number = int(round(frames / frame_interval, 0))

    frame_indices = []
    for i in range(0, frames, frame_interval):
        cap.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = cap.read()
        print('Total frame number:' + total_number.__str__(), ', complete', round((i * 1.0 / frames) * 100, 3), '%')
        cv2.imwrite(out_path + "/frame_" + i.__str__().zfill(5) + out_type, frame)
        frame_indices.append(i)
    cap.release()

    fout = open(out_path + "/summary.txt", 'w')
    fout.write("Video name:" + video_path + "\n")
    fout.write("Frames in total:" + frames.__str__() + "\n")
    fout.write("FPS:" + fps.__str__() + "\n")
    fout.write("Seconds in total:" + round(frames * 1.0 / fps, 3).__str__() + "\n")
    fout.write("Frame width:" + video_width.__str__() + "\n")
    fout.write("Frame height:" + video_height.__str__() + "\n")
    fout.write("Output frame number:" + len(frame_indices).__str__() + "\n")
    for i in range(len(frame_indices)):
        fout.write(frame_indices[i].__str__() + "\t" + round(frame_indices[i] * 1.0 / fps, 3).__str__() + "\n")
    fout.close()

    print("\n==========Summary Info==========")
    print('Frames in total:', frames)
    print('FPS:', fps)
    print('Frame width:', video_width)
    print('Frame height', video_height)
    print("Output frame number:", len(frame_indices))
