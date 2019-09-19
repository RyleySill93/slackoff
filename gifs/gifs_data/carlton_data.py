from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

carlton = TrackedElement(id=1)
tracked_elements = [carlton]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=97, y=127, height=70)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=98, y=127, height=70)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=96, y=130, height=70)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=98, y=130, height=70)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=108, y=130, height=70)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=112, y=129, height=70)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=123, y=135, height=70)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=122, y=133, height=70)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=113, y=129, height=70)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=106, y=127, height=70)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=98, y=125, height=70)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=97, y=125, height=70)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=100, y=129, height=70)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=101, y=131, height=70)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=102, y=132, height=70)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=99, y=133, height=70)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=90, y=139, height=70)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=84, y=142, height=70)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=74, y=145, height=70)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=73, y=147, height=70)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=80, y=138, height=70)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=88, y=133, height=70)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=97, y=126, height=70)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=carlton.id, x=96, y=123, height=70)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=carlton.id, x=10)
]

carlton = ImageData(
    type='carlton',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/carlton.gif',
    adjustments=adjustments,
)

