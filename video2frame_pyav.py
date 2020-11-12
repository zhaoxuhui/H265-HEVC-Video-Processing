import av

if __name__ == '__main__':
    video_path = "./D01_20201011131153.mp4"
    out_path = "./frames"
    frame_interval = 500

    container = av.open(video_path)
    # 获取要提取的视频流对象
    stream = container.streams.video[0]
    fps = stream.base_rate  # 帧率
    frame_width = stream.width  # 帧宽
    frame_height = stream.height  # 帧高
    total_time_in_second = stream.duration * 1.0 * stream.time_base  # 视频总长
    total_frame = int(total_time_in_second * fps) + 1  # 视频总帧数
    iter_time = int(total_frame / frame_interval) + 1  # 需要迭代的次数
    print('Total time in second:', round(total_time_in_second, 3))

    counter = 0
    frame_indices = []
    for frame in container.decode(video=0):
        if frame.index % frame_interval == 0:
            counter += 1
            frame_indices.append(frame.index)
            print(counter, '/', iter_time)
            # to_image()函数返回的其实是PIL类型的影像，因此，这里的save()函数其实是PIL的Image类型的成员函数，和PyAV无关
            # 因此，如果需要修改什么保存相关设置的话，按照PIL的API进行
            frame.to_image().save(out_path + "/frame-%05d.jpg" % frame.index)

    fout = open(out_path + "/summary.txt", 'w')
    fout.write("Video name:" + video_path + "\n")
    fout.write("Frames in total:" + total_frame.__str__() + "\n")
    fout.write("FPS:" + fps.__str__() + "\n")
    fout.write("Seconds in total:" + round(total_time_in_second, 3).__str__() + "\n")
    fout.write("Frame width:" + frame_width.__str__() + "\n")
    fout.write("Frame height:" + frame_height.__str__() + "\n")
    fout.write("Output frame number:" + iter_time.__str__() + "\n")
    for i in range(len(frame_indices)):
        fout.write(frame_indices[i].__str__() + "\t" + round(frame_indices[i] * 1.0 / fps, 3).__str__() + "\n")
    fout.close()

    print("\n==========Summary Info==========")
    print('Frames in total:', total_frame)
    print('FPS:', fps)
    print('Frame width:', frame_width)
    print('Frame height', frame_height)
    print("Output frame number:", len(frame_indices))
