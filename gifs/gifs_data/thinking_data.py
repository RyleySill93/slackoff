from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

dude = TrackedElement(id=1)
tracked_elements = [dude]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=261, y=126, height=168)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=263, y=125, height=168)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=261, y=121, height=168)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=261, y=121, height=168)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=264, y=124, height=168)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=264, y=125, height=168)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=264, y=125, height=168)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=264, y=125, height=168)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=265, y=128, height=168)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=263, y=132, height=168)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=264, y=134, height=168)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=263, y=132, height=168)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=262, y=126, height=168)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=260, y=123, height=168)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=261, y=117, height=168)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=259, y=111, height=168)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=259, y=105, height=168)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=259, y=101, height=168)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=259, y=101, height=168)])
]

adjustments = [
    TrackedElementPosition(tracked_element_id=dude.id, x=15, height=30, y=-15)
]

thinking = ImageData(
    type='thinking',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/thinking.gif',
    adjustments=adjustments,
)

