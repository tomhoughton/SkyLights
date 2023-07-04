import os
import PIL.Image, PIL.ImageDraw

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

    def display_frame_data(self):
        print(self.frames)