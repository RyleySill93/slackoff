from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition


kid = TrackedElement(
    id=1,
)

tracked_elements = [kid]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=100, y=70, height=130)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=97, y=69, height=130)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=98, y=71, height=130)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=99, y=68, height=130)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=94, y=66, height=130)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=93, y=67, height=130)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=95, y=69, height=130)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=96, y=71, height=130)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=97, y=71, height=130)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=96, y=70, height=130)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=99, y=73, height=130)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=100, y=73, height=130)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=99, y=69, height=130)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=98, y=71, height=130)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=118, y=86, height=175)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=86, height=175)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=86, height=175)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=116, y=87, height=175)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=84, height=175)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=119, y=87, height=175)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=118, y=86, height=175)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=83, height=175)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=86, height=175)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=121, y=88, height=175)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=85, height=175)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=113, y=86, height=175)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=87, height=175)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=113, y=85, height=175)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=88, height=175)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=113, y=86, height=175)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=116, y=87, height=175)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=117, y=88, height=175)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=88, height=175, brightness=0.95)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175, brightness=0.80)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175, brightness=0.60)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175, brightness=0.40)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175, brightness=0.30)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=kid.id, x=115, y=87, height=175, brightness=0.15)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=kid.id)
]

computer_kid = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/computer_kid.gif',
    adjustments=adjustments,
)
