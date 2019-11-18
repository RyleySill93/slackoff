from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

jav = TrackedElement(id=1)
tracked_elements = [jav]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=77, y=91, height=58)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=81, y=91, height=63)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=84, y=91, height=66)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=88, y=92, height=64)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=90, y=92, height=68)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=93, y=93, height=68)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=94, y=96, height=69)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=94, y=96, height=70)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=95, y=95, height=72)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=95, y=93, height=72)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=95, y=93, height=72)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=95, y=94, height=72)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=97, y=93, height=73)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=97, y=93, height=75)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=98, y=93, height=75)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=98, y=94, height=77)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=100, y=93, height=80)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=100, y=94, height=81)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=99, y=94, height=80)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=100, y=94, height=82)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=99, y=94, height=83)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=99, y=93, height=83)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=98, y=94, height=84)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=98, y=94, height=85)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=97, y=94, height=89)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=97, y=95, height=90)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=97, y=96, height=93)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=96, y=96, height=93)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=96, y=99, height=95)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jav.id, x=96, y=100, height=97)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=jav.id, height=50, rotation=-10, x=-10)
]

image_data = ImageData(
    type='javert',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/javert.gif',
    foreground_image_path='pics/javert_mask.gif',
    adjustments=adjustments,
    foreground_indicies=[*range(len(frames_data))],
    width=175,
    height=200,
)
