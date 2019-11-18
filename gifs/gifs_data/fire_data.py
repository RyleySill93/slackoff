from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition


donald = TrackedElement(
    id=1,
)

tracked_elements = [donald]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=227, y=83, height=130)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=205, y=75, height=130)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=184, y=64, height=130)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=167, y=77, height=130)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=157, y=89, height=130)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=159, y=70, height=130)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=161, y=69, height=130)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=167, y=73, height=130)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=68, height=130)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=77, height=20)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=76, height=20)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=77, height=20)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=76, height=20)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=174, y=76, height=20)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=173, y=76, height=20)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=172, y=76, height=20)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=172, y=76, height=20)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=172, y=76, height=20)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=173, y=66, height=130)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=172, y=64, height=130)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=173, y=63, height=130)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=176, y=63, height=130)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=180, y=63, height=130)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=185, y=63, height=130)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=donald.id, x=186, y=63, height=130)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=donald.id)
]

image_data = ImageData(
    type='fire',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/fire.gif',
    adjustments=adjustments,
    width=340,
    height=347,
)
