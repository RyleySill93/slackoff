from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition


leo = TrackedElement(
    id=1,
)

tracked_elements = [leo]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=256, y=78, height=123)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=258, y=82, height=123)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=258, y=81, height=123)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=258, y=81, height=123)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=258, y=80, height=123)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=259, y=80, height=123)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=259, y=80, height=123)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=260, y=78, height=123)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=259, y=78, height=123)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=259, y=78, height=123)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=260, y=79, height=123)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=260, y=77, height=123)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=261, y=77, height=123)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=260, y=78, height=123)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=leo.id, x=260, y=78, height=123)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=leo.id, height=10, y=-10, x=-8)
]

toast = ImageData(
    type='toast',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/toast.gif',
    foreground_image_path='pics/toast_mask.gif',
    adjustments=adjustments,
)
