from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition


shia = TrackedElement(
    id=1,
)

tracked_elements = [shia]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=76, height=92)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=shia.id, x=143, y=78, height=92)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=shia.id, x=0, height=20)
]

magic = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/magic.gif',
    foreground_image_path='pics/magic_mask.gif',
    adjustments=adjustments,
)
