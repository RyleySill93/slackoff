from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

trump_face = TrackedElement(id=1)
tracked_elements = [trump_face]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=95, y=95, height=170)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=91, y=94, height=170)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=90, y=95, height=170)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=91, y=97, height=170)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=91, y=96, height=170)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=93, y=98, height=170)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=94, y=97, height=170)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=94, y=97, height=170)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=96, y=97, height=170)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=105, y=96, height=170)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=110, y=95, height=170)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=129, y=97, height=170, rotation=-12)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=150, y=92, height=170, rotation=-15)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=161, y=91, height=170, rotation=-18)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=188, y=98, height=170, rotation=-21)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=199, y=99, height=170, rotation=-24)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=215, y=101, height=170, rotation=-24)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=220, y=102, height=170, rotation=-24)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=224, y=101, height=170, rotation=-24)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=226, y=103, height=170, rotation=-24)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=231, y=102, height=170, rotation=-21)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=231, y=102, height=170, rotation=-18)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=239, y=104, height=170, rotation=-15)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=241, y=105, height=170, rotation=-12)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=248, y=100, height=170, rotation=-9)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=248, y=105, height=170, rotation=-6)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=260, y=107, height=170, rotation=-3)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=260, y=107, height=170)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=271, y=111, height=170)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=271, y=110, height=170)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=279, y=102, height=170)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=285, y=102, height=170)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=299, y=102, height=170)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=304, y=104, height=170)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=320, y=106, height=170)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=329, y=111, height=170)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=353, y=117, height=170)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=367, y=121, height=170)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=411, y=129, height=170)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=433, y=131, height=170)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=trump_face.id, x=473, y=134, height=170)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=trump_face.id, height=20, x=-30)
]

trump = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/trump.gif',
    foreground_image_path='pics/trump_mask.gif',
    adjustments=adjustments,
    foreground_indicies=list(range(len(frames_data))),
)

