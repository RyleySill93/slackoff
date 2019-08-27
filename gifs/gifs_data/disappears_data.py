from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

homer = TrackedElement(id=1)
tracked_elements = [homer]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=242, y=100, height=180)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=244, y=100, height=180)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=240, y=100, height=180)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=241, y=100, height=180)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=248, y=104, height=180)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=248, y=104, height=180)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=250, y=105, height=180)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=248, y=107, height=180)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=249, y=106, height=180)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=252, y=108, height=180)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=255, y=111, height=180)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=257, y=112, height=180)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=259, y=113, height=180)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=262, y=115, height=180)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=262, y=115, height=180)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=266, y=119, height=180)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=269, y=118, height=180)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=273, y=121, height=180)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=122, height=180)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=278, y=122, height=180)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=279, y=122, height=180)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=275, y=123, height=180)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=121, height=180)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=277, y=121, height=180)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=280, y=123, height=180)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=277, y=123, height=180)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=277, y=123, height=180)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=272, y=123, height=180)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=272, y=122, height=180)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=266, y=124, height=180)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=265, y=123, height=180)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=265, y=123, height=180)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=267, y=123, height=180)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=268, y=124, height=180)]),
    FrameData(index=41, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=268, y=123, height=180)]),
    FrameData(index=42, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=270, y=123, height=180)]),
    FrameData(index=43, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=272, y=122, height=180)]),
    FrameData(index=44, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=272, y=122, height=180)]),
    FrameData(index=45, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=123, height=180)]),
    FrameData(index=46, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=123, height=180)]),
    FrameData(index=47, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=123, height=180)]),
    FrameData(index=48, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=123, height=180)]),
    FrameData(index=49, tracked_element_positions=[TrackedElementPosition(tracked_element_id=homer.id, x=276, y=123, height=180)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=homer.id, x=8)
]

disappears = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/homer.gif',
    foreground_image_path='pics/homermask.gif',
    adjustments=adjustments,
    foreground_indicies=[*range(23, len(frames_data))],
)

