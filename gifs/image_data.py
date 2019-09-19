class ImageData:
    def __init__(
        self,
        type,
        background_image_path,
        frames_data,
        tracked_elements,
        adjustments,
        foreground_image_path=None,
        foreground_indicies=[],
    ):
        self.type = type
        self.background_image_path = background_image_path
        self.frames_data = frames_data
        self.tracked_elements = tracked_elements
        self.adjustments = adjustments
        self.foreground_image_path = foreground_image_path
        self.foreground_indicies = foreground_indicies or list(range(0, len(frames_data)))

    def get_frame(self, frame_index):

        for frame in self.frames_data:
            if frame.index == frame_index:
                return frame

        return None

    def get_tracked_element_position(self, tracked_element_id, frame_index):
        frame = self.get_frame(frame_index)

        if not frame:
            return None

        for tracked_element_position in frame.tracked_element_positions:
            if tracked_element_position.tracked_element_id == tracked_element_id:
                return tracked_element_position

        raise ValueError('tracked element position not found')

    def get_tracked_element_adjustment(self, tracked_element_id):
        for adjustment in self.adjustments:
            if adjustment.tracked_element_id == tracked_element_id:
                return adjustment

        return None


class FrameData:
    def __init__(self, tracked_element_positions, index):
        self.index = index
        self.tracked_element_positions = tracked_element_positions


class TrackedElement:
    def __init__(
        self,
        id,
        image_file=None,
        text=None,
    ):
        self.id = id
        self.image_file = image_file
        self.text = text


class TrackedElementPosition:
    def __init__(
        self,
        tracked_element_id,
        x=None,
        y=None,
        z=None,
        width=None,
        height=None,
        rotation=None,
        brightness=None,
    ):
        self.tracked_element_id = tracked_element_id
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.rotation = rotation
        self.brightness = brightness
