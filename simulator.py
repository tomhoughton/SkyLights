import os
import PIL.Image, PIL.ImageDraw
import cv2

class Simulator:
    def __init__(self) -> None:
        
        self.frame_eport_path = os.path.join('frames')
        
        # View port height and width:
        self.height = 250
        self.width = self.height * 4

        # Stores all frames file names:
        self.frames = [];
        pass

    def create_frame(self, color01, color02, color03, color04, frame_name):
        new_frame = PIL.Image.new(
            'RGB',
            (self.width, self.height),
            (0, 0, 0)
        )

        for y in range(0, self.height):
            for x in range(0, self.width):
                # Color each square:
                if (x > 0 and x < self.height * 1):
                    new_frame.putpixel((x, y), color01)
                elif (x > self.height * 1 and x < self.height * 2):
                    new_frame.putpixel((x, y), color02)
                elif (x > self.height * 2 and x < self.height * 3):
                    new_frame.putpixel((x, y), color03)
                elif (x > self.height * 3 and x < self.height * 4):
                    new_frame.putpixel((x, y), color04)
        
        frame_file_name = "{}.jpg".format(frame_name)
        new_frame.save(
            os.path.join(self.frame_eport_path,frame_file_name
        ))
        self.frames.append(frame_file_name)

    def write_video(self):
        if len(self.frames) > 0:
            # Store the opened frames:
            new_frames = []

            for frame in self.frames:
                # Open frame:
                img = cv2.imread(os.path.join(self.frame_eport_path, frame))
                hieght, width, layers = img.shape
                size = (width, height)
                new_frames.append(img)

            # Create a video out object:
            out = cv2.VideoWriter('project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 60, size)

            # Write frames to out:
            for i in range(len(new_frames)):
                out.write(new_frames[i])

            # Release the video:
            out.release()

    def display_frame_data(self):
        print(self.frames)