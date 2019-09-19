from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

guy = TrackedElement(id=1)
tracked_elements = [guy]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=295, y=143, height=196)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=292, y=142, height=196)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=292, y=142, height=196)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=293, y=141, height=196)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=292, y=142, height=196)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=294, y=143, height=196)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=296, y=141, height=196)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=294, y=139, height=196)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=296, y=141, height=196)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=297, y=139, height=196)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=298, y=140, height=196)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=298, y=141, height=196)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=298, y=142, height=196)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=296, y=142, height=196)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=guy.id, x=293, y=140, height=196)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=guy.id, height=30)
]

clapping = ImageData(
    type='clapping',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/clapping.gif',
    foreground_image_path='pics/clapping_mask.gif',
    adjustments=adjustments,
)
