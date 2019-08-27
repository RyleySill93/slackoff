from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

neil = TrackedElement(id=1)
tracked_elements = [neil]

frames_data = [
    FrameData(index=0, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=221, y=165, height=212)]),
    FrameData(index=1, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=221, y=165, height=212)]),
    FrameData(index=2, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=221, y=165, height=212)]),
    FrameData(index=3, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=222, y=157, height=212)]),
    FrameData(index=4, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=222, y=157, height=212)]),
    FrameData(index=5, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=224, y=145, height=212)]),
    FrameData(index=6, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=224, y=145, height=212)]),
    FrameData(index=7, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=227, y=144, height=212)]),
    FrameData(index=8, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=227, y=144, height=212)]),
    FrameData(index=9, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=227, y=144, height=212)]),
    FrameData(index=10, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=231, y=145, height=212)]),
    FrameData(index=11, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=232, y=145, height=212)]),
    FrameData(index=12, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=232, y=145, height=212)]),
    FrameData(index=13, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=233, y=153, height=212)]),
    FrameData(index=14, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=233, y=153, height=212)]),
    FrameData(index=15, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=234, y=152, height=212)]),
    FrameData(index=16, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=236, y=155, height=212)]),
    FrameData(index=17, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=235, y=155, height=212)]),
    FrameData(index=18, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=237, y=159, height=212)]),
    FrameData(index=19, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=237, y=161, height=212)]),
    FrameData(index=20, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=237, y=161, height=212)]),
    FrameData(index=21, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=240, y=163, height=212)]),
    FrameData(index=22, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=242, y=164, height=212)]),
    FrameData(index=23, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=241, y=171, height=212)]),
    FrameData(index=24, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=243, y=173, height=212)]),
    FrameData(index=25, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=245, y=172, height=212)]),
    FrameData(index=26, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=245, y=176, height=212)]),
    FrameData(index=27, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=247, y=182, height=212)]),
    FrameData(index=28, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=247, y=187, height=212)]),
    FrameData(index=29, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=247, y=187, height=212)]),
    FrameData(index=30, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=247, y=193, height=212)]),
    FrameData(index=31, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=244, y=196, height=212)]),
    FrameData(index=32, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=246, y=197, height=212)]),
    FrameData(index=33, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=244, y=198, height=212)]),
    FrameData(index=34, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=244, y=198, height=212)]),
    FrameData(index=35, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=240, y=202, height=212)]),
    FrameData(index=36, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=240, y=202, height=212)]),
    FrameData(index=37, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=240, y=202, height=212)]),
    FrameData(index=38, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=238, y=203, height=212)]),
    FrameData(index=39, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=238, y=205, height=212)]),
    FrameData(index=40, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=238, y=205, height=212)]),
    FrameData(index=41, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=236, y=204, height=212)]),
    FrameData(index=42, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=237, y=205, height=212)]),
    FrameData(index=43, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=236, y=206, height=212)]),
    FrameData(index=44, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=236, y=206, height=212)]),
    FrameData(index=45, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=238, y=206, height=212)]),
    FrameData(index=46, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=238, y=208, height=212)]),
    FrameData(index=47, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=239, y=209, height=212)]),
    FrameData(index=48, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=239, y=209, height=212)]),
    FrameData(index=49, tracked_element_positions=[TrackedElementPosition(tracked_element_id=neil.id, x=239, y=209, height=212)]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=neil.id, height=50, y=10)
]

mind_blown = ImageData(
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/mind_blown.gif',
    foreground_image_path='pics/mind_blown_mask.gif',
    adjustments=adjustments,
)

