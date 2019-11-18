from gifs.image_data import ImageData, FrameData, TrackedElement, TrackedElementPosition

guy = TrackedElement(id=1)
kid = TrackedElement(id=2)
chick = TrackedElement(id=3)
tracked_elements = [guy, kid, chick]

frames_data = [
    FrameData(index=0, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=66, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=224, y=117),
        TrackedElementPosition(tracked_element_id=chick.id, x=314, y=86),
    ]),
    FrameData(index=1, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=67, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=228, y=117),
        TrackedElementPosition(tracked_element_id=chick.id, x=300, y=87),
    ]),
    FrameData(index=2, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=68, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=227, y=115),
        TrackedElementPosition(tracked_element_id=chick.id, x=283, y=91),
    ]),
    FrameData(index=3, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=68, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=208, y=115),
        TrackedElementPosition(tracked_element_id=chick.id, x=282, y=89),
    ]),
    FrameData(index=4, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=70, y=65),
        TrackedElementPosition(tracked_element_id=kid.id, x=188, y=119),
        TrackedElementPosition(tracked_element_id=chick.id, x=282, y=87),
    ]),
    FrameData(index=5, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=78, y=66),
        TrackedElementPosition(tracked_element_id=kid.id, x=175, y=125),
        TrackedElementPosition(tracked_element_id=chick.id, x=288, y=84),
    ]),
    FrameData(index=6, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=86, y=66),
        TrackedElementPosition(tracked_element_id=kid.id, x=163, y=125),
        TrackedElementPosition(tracked_element_id=chick.id, x=297, y=82),
    ]),
    FrameData(index=7, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=94, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=151, y=127),
        TrackedElementPosition(tracked_element_id=chick.id, x=303, y=81),
    ]),
    FrameData(index=8, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=105, y=69),
        TrackedElementPosition(tracked_element_id=kid.id, x=142, y=135),
        TrackedElementPosition(tracked_element_id=chick.id, x=306, y=82),
    ]),
    FrameData(index=9, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=113, y=70),
        TrackedElementPosition(tracked_element_id=kid.id, x=146, y=135),
        TrackedElementPosition(tracked_element_id=chick.id, x=310, y=83),
    ]),
    FrameData(index=10, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=111, y=71),
        TrackedElementPosition(tracked_element_id=kid.id, x=164, y=145),
        TrackedElementPosition(tracked_element_id=chick.id, x=310, y=83),
    ]),
    FrameData(index=11, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=96, y=68),
        TrackedElementPosition(tracked_element_id=kid.id, x=198, y=157),
        TrackedElementPosition(tracked_element_id=chick.id, x=312, y=82),
    ]),
    FrameData(index=12, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=89, y=68),
        TrackedElementPosition(tracked_element_id=kid.id, x=218, y=156),
        TrackedElementPosition(tracked_element_id=chick.id, x=314, y=83),
    ]),
    FrameData(index=13, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=84, y=69),
        TrackedElementPosition(tracked_element_id=kid.id, x=236, y=146),
        TrackedElementPosition(tracked_element_id=chick.id, x=313, y=83),
    ]),
    FrameData(index=14, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=81, y=66),
        TrackedElementPosition(tracked_element_id=kid.id, x=243, y=142),
        TrackedElementPosition(tracked_element_id=chick.id, x=312, y=86),
    ]),
    FrameData(index=15, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=82, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=247, y=138),
        TrackedElementPosition(tracked_element_id=chick.id, x=310, y=91),
    ]),
    FrameData(index=16, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=85, y=63),
        TrackedElementPosition(tracked_element_id=kid.id, x=248, y=131),
        TrackedElementPosition(tracked_element_id=chick.id, x=304, y=92),
    ]),
    FrameData(index=17, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=88, y=63),
        TrackedElementPosition(tracked_element_id=kid.id, x=236, y=126),
        TrackedElementPosition(tracked_element_id=chick.id, x=300, y=93),
    ]),
    FrameData(index=18, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=91, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=208, y=125),
        TrackedElementPosition(tracked_element_id=chick.id, x=310, y=91),
    ]),
    FrameData(index=19, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=93, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=183, y=129),
        TrackedElementPosition(tracked_element_id=chick.id, x=317, y=86),
    ]),
    FrameData(index=20, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=95, y=65),
        TrackedElementPosition(tracked_element_id=kid.id, x=164, y=120),
        TrackedElementPosition(tracked_element_id=chick.id, x=328, y=82),
    ]),
    FrameData(index=21, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=100, y=66),
        TrackedElementPosition(tracked_element_id=kid.id, x=151, y=120),
        TrackedElementPosition(tracked_element_id=chick.id, x=335, y=80),
    ]),
    FrameData(index=22, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=107, y=70),
        TrackedElementPosition(tracked_element_id=kid.id, x=142, y=125),
        TrackedElementPosition(tracked_element_id=chick.id, x=337, y=79),
    ]),
    FrameData(index=23, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=125, y=76),
        TrackedElementPosition(tracked_element_id=kid.id, x=131, y=130),
        TrackedElementPosition(tracked_element_id=chick.id, x=343, y=78),
    ]),
    FrameData(index=24, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=128, y=78),
        TrackedElementPosition(tracked_element_id=kid.id, x=131, y=142),
        TrackedElementPosition(tracked_element_id=chick.id, x=348, y=78),
    ]),
    FrameData(index=25, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=123, y=74),
        TrackedElementPosition(tracked_element_id=kid.id, x=135, y=150),
        TrackedElementPosition(tracked_element_id=chick.id, x=347, y=77),
    ]),
    FrameData(index=26, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=113, y=70),
        TrackedElementPosition(tracked_element_id=kid.id, x=154, y=156),
        TrackedElementPosition(tracked_element_id=chick.id, x=354, y=79),
    ]),
    FrameData(index=27, tracked_element_positions=[
        TrackedElementPosition(tracked_element_id=guy.id, x=104, y=64),
        TrackedElementPosition(tracked_element_id=kid.id, x=167, y=149),
        TrackedElementPosition(tracked_element_id=chick.id, x=359, y=80),
    ]),
]

adjustments = [
    TrackedElementPosition(tracked_element_id=guy.id, height=45),
    TrackedElementPosition(tracked_element_id=kid.id, height=45),
    TrackedElementPosition(tracked_element_id=chick.id, height=55, x=5),
]

image_data = ImageData(
    type='bullying',
    frames_data=frames_data,
    tracked_elements=tracked_elements,
    background_image_path='pics/bullying.gif',
    adjustments=adjustments,
    width=432,
    height=288,
)
