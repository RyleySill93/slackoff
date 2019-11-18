from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

dude = TrackedElement(id=1)
tracked_elements = [dude]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=92, y=68, height=41)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=91, y=65, height=41)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=90, y=65, height=41)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=91, y=63, height=41)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=91, y=63, height=41)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=91, y=63, height=41)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=92, y=59, height=41)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=94, y=60, height=41)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=95, y=60, height=41)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=97, y=61, height=41)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=99, y=60, height=41)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=62, height=41)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=61, height=41)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=111, y=61, height=41)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=113, y=60, height=41)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=114, y=56, height=41)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=116, y=55, height=41)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=118, y=51, height=41)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=119, y=47, height=41)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=121, y=40, height=41)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=120, y=34, height=41)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=119, y=31, height=41)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=117, y=30, height=41)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=116, y=29, height=41)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=113, y=30, height=41)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=109, y=31, height=41)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=105, y=33, height=41)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=36, height=41)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=99, y=37, height=41)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=97, y=37, height=41)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=95, y=36, height=41)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=92, y=34, height=41)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=90, y=30, height=41)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=88, y=26, height=41)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=88, y=22, height=41)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=85, y=17, height=41)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=83, y=17, height=41)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=83, y=18, height=41)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=82, y=18, height=41)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=82, y=19, height=41)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=82, y=21, height=41)]),
    FrameData(index=41, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=82, y=23, height=41)]),
    FrameData(index=42, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=85, y=22, height=41)]),
    FrameData(index=43, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=89, y=23, height=41)]),
    FrameData(index=44, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=92, y=22, height=41)]),
    FrameData(index=45, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=96, y=22, height=41)]),
    FrameData(index=46, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=99, y=23, height=41)]),
    FrameData(index=47, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=98, y=23, height=41)]),
    FrameData(index=48, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=25, height=41)]),
    FrameData(index=49, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=101, y=24, height=41)]),
    FrameData(index=50, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=101, y=26, height=41)]),
    FrameData(index=51, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=27, height=41)]),
    FrameData(index=52, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=27, height=41)]),
    FrameData(index=53, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=103, y=25, height=41)]),
    FrameData(index=54, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=103, y=27, height=41)]),
    FrameData(index=55, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=104, y=27, height=41)]),
    FrameData(index=56, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=27, height=41)]),
    FrameData(index=57, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=29, height=41)]),
    FrameData(index=58, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=26, height=41)]),
    FrameData(index=59, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=107, y=28, height=41)]),
    FrameData(index=60, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=107, y=29, height=41)]),
    FrameData(index=61, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=107, y=28, height=41)]),
    FrameData(index=62, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=108, y=28, height=41)]),
    FrameData(index=63, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=109, y=32, height=41)]),
    FrameData(index=64, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=106, y=35, height=41)]),
    FrameData(index=65, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=103, y=37, height=41)]),
    FrameData(index=66, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=101, y=36, height=41)]),
    FrameData(index=67, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=102, y=36, height=41)]),
    FrameData(index=68, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=103, y=37, height=41)]),
    FrameData(index=69, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=99, y=38, height=41)]),
    FrameData(index=70, tracked_element_positions=[TrackedElementPosition(tracked_element_id=dude.id, x=101, y=24, height=41)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=dude.id, height=20)
]

image_data = ImageData(
    type='chimp',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/chimp.gif',
    adjustments=adjustments,
    foreground_indicies=list(range(len(frames_data))),
    width=225,
    height=200,
)

