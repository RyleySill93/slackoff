from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

vince = TrackedElement(id=1)
tracked_elements = [vince]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=125, y=85, height=18)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=126, y=82, height=21)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=129, y=80, height=23)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=129, y=78, height=24)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=130, y=74, height=25)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=129, y=68, height=26)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=127, y=63, height=27)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=126, y=60, height=28)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=125, y=58, height=29)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=124, y=58, height=32)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=118, y=55, height=34)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=112, y=55, height=37)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=111, y=52, height=40)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=111, y=47, height=43)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=116, y=43, height=43)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=119, y=43, height=44)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=122, y=46, height=44)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=126, y=51, height=47)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=135, y=54, height=51)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=149, y=52, height=53)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=155, y=51, height=56)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=155, y=45, height=57)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=152, y=39, height=57)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=151, y=35, height=56)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=151, y=37, height=54)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=149, y=43, height=57)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=142, y=48, height=57)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=128, y=47, height=58)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=116, y=48, height=60)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=112, y=45, height=60)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=116, y=39, height=58)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=121, y=37, height=55)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=122, y=39, height=55)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=vince.id, x=118, y=44, height=57)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=vince.id, height=30)
]

strut = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/strut.gif',
    adjustments=adjustments,
)

