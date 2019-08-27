from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

dude = TrackedElement(id=1)
tracked_elements = [dude]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=275, y=74, height=150, rotation=5)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=271, y=66, height=150, rotation=10)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=268, y=64, height=150, rotation=15)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=233, y=81, height=150, rotation=20)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=216, y=83, height=150, rotation=25)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=201, y=78, height=150, rotation=30)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=181, y=80, height=150, rotation=35)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=163, y=81, height=150, rotation=40)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=150, y=86, height=150, rotation=45)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=134, y=101, height=150, rotation=50)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=113, y=111, height=150, rotation=55)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=112, y=112, height=150, rotation=60)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=124, height=150, rotation=60)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=105, y=138, height=150, rotation=60)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=143, height=150, rotation=60)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=101, y=151, height=150, rotation=65)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=94, y=169, height=150, rotation=65)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=82, y=185, height=150, rotation=65)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=dude.id, x=-30, height=40)
]

hide = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/hide.gif',
    foreground_image_path='pics/hide_mask.gif',
    adjustments=adjustments,
    foreground_indicies=list(range(len(frames_data))),
)

