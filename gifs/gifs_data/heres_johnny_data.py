from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

jack = TrackedElement(id=1)
tracked_elements = [jack]

frames_data = [
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=306, y=114, height=135)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=286, y=126, height=120)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=283, y=133, height=115)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=282, y=161, height=120)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=290, y=166, height=120)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=175, height=115)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=303, y=169, height=115)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=288, y=146, height=110)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=270, y=152, height=108)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=253, y=166, height=100)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=250, y=161, height=100)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=258, y=156, height=102)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=269, y=159, height=104)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=288, y=164, height=108)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=311, y=173, height=105)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=344, y=165, height=105)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=355, y=153, height=105)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=376, y=153, height=108)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=380, y=150, height=108)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=380, y=150, height=107)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=380, y=156, height=103)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=380, y=162, height=102)]),
    FrameData(index=41, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=375, y=169, height=101)]),
    FrameData(index=42, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=377, y=179, height=98)]),
    FrameData(index=43, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=385, y=177, height=100)]),
    FrameData(index=44, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=430, y=180, height=100)]),
    FrameData(index=45, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=437, y=179, height=103)]),
    FrameData(index=46, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=459, y=204, height=105)]),
    FrameData(index=47, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=470, y=213, height=105)]),
    FrameData(index=48, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=470, y=213, height=110)]),
    FrameData(index=49, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=469, y=193, height=120)]),
    FrameData(index=50, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=422, y=209, height=130)]),
    FrameData(index=51, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=365, y=185, height=135)]),
    FrameData(index=52, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=288, y=187, height=132)]),
    FrameData(index=53, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=260, y=200, height=128)]),
    FrameData(index=54, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=251, y=196, height=130)]),
    FrameData(index=55, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=266, y=193, height=135)]),
    FrameData(index=56, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=285, y=201, height=140)]),
    FrameData(index=57, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=306, y=223, height=150)]),
    FrameData(index=58, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=326, y=245, height=160)]),
    FrameData(index=59, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=340, y=256, height=163)]),
    FrameData(index=60, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=352, y=256, height=167)]),
    FrameData(index=80, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=110, height=430)]),
    FrameData(index=81, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=100, height=430)]),
    FrameData(index=82, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=90, height=430)]),
    FrameData(index=83, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=320, y=110, height=430)]),
    FrameData(index=84, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=90, height=430)]),
    FrameData(index=85, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=110, height=430)]),
    FrameData(index=86, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=100, height=430)]),
    FrameData(index=87, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=320, y=110, height=430)]),
    FrameData(index=88, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=90, height=430)]),
    FrameData(index=89, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=110, height=430)]),
    FrameData(index=90, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=320, y=100, height=430)]),
    FrameData(index=91, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=110, height=430)]),
    FrameData(index=92, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=90, height=430)]),
    FrameData(index=93, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=110, height=430)]),
    FrameData(index=94, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=320, y=110, height=430)]),
    FrameData(index=95, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=340, y=90, height=430)]),
    FrameData(index=96, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=110, height=430)]),
    FrameData(index=97, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=300, y=110, height=430)]),
    FrameData(index=98, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=290, y=140, height=430)]),
    FrameData(index=99, tracked_element_positions=[TrackedElementPosition(tracked_element_id=jack.id, x=310, y=110, height=430)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=jack.id, height=40)
]

heres_johnny = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/johnny.gif',
    foreground_image_path='pics/johnny_mask.gif',
    adjustments=adjustments,
    foreground_indicies=[el.index for el in frames_data]
)

