from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

kid = TrackedElement(id=1)
tracked_elements = [kid]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=177, y=85, height=102)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=177, y=85, height=102)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=176, y=85, height=102)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=176, y=85, height=102)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=177, y=85, height=102)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=177, y=85, height=102)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=176, y=83, height=102)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=176, y=83, height=102)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=176, y=83, height=102)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=175, y=83, height=102)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=174, y=82, height=102)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=174, y=82, height=102)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=174, y=81, height=102)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=174, y=82, height=102)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=173, y=82, height=102)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=173, y=82, height=102)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=173, y=81, height=102)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=173, y=82, height=102)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=172, y=82, height=102)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=173, y=82, height=102)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=kid.id, x=-10, y=-10, height=10, rotation=8)
]

begging = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/begging.gif',
    adjustments=adjustments,
    foreground_indicies=list(range(len(frames_data))),
)

