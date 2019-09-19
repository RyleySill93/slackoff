from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

supahot = TrackedElement(id=1)
tracked_elements = [supahot]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=158, y=88, height=90)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=157, y=88, height=90)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=155, y=88, height=90)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=155, y=88, height=90)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=155, y=88, height=90)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=152, y=87, height=90)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=151, y=87, height=90)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=149, y=85, height=90)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=146, y=84, height=90)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=142, y=84, height=90)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=139, y=83, height=90)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=138, y=83, height=90)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=136, y=82, height=90)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=133, y=84, height=90)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=132, y=84, height=90)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=129, y=83, height=90)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=130, y=82, height=90)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=127, y=80, height=90)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=125, y=79, height=90)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=124, y=77, height=90)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=123, y=75, height=90)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=123, y=75, height=90)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=121, y=72, height=90)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=120, y=69, height=90)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=120, y=66, height=90)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=121, y=63, height=90)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=121, y=63, height=90)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=124, y=60, height=90)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=124, y=60, height=90)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=127, y=58, height=90)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=129, y=58, height=90)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=129, y=58, height=90)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=130, y=61, height=90)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=130, y=61, height=90)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=130, y=62, height=90)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=133, y=65, height=90)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=137, y=67, height=90)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=140, y=70, height=90)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=144, y=73, height=90)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=149, y=76, height=90)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=149, y=76, height=90)]),
    FrameData(index=41, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=147, y=73, height=90)]),
    FrameData(index=42, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=150, y=76, height=90)]),
    FrameData(index=43, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=155, y=79, height=90)]),
    FrameData(index=44, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=155, y=79, height=90)]),
    FrameData(index=45, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=158, y=80, height=90)]),
    FrameData(index=46, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=160, y=83, height=90)]),
    FrameData(index=47, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=160, y=85, height=90)]),
    FrameData(index=48, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=160, y=85, height=90)]),
    FrameData(index=49, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=159, y=86, height=90)]),
    FrameData(index=50, tracked_element_positions=[TrackedElementPosition(tracked_element_id=supahot.id, x=159, y=86, height=90)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=supahot.id)
]

supa_hot_fire = ImageData(
    type='supa_hot_fire',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/rap.gif',
    foreground_image_path='pics/rapmask.gif',
    adjustments=adjustments,
    foreground_indicies=[*range(24, 50)],
)

