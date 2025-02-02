from manim import DOWN, ORANGE, UP, WHITE, YELLOW, FadeIn, FadeOut, Scene, Text, Write

from visual_data_lessons.config import DEFAULT_FONT


class OutroScene(Scene):
    """
    A scene for displaying a thank-you message and a call to action at the end of the video.

    This outro is designed to leave space for YouTube end screens, allowing suggested videos
    and the subscribe button to be placed within the YouTube interface.

    Methods
    -------
    display_outro() -> None
        Displays a thank-you message and a subscribe prompt before fading out.
    construct() -> None
        Calls the display_outro method to construct the scene.
    """

    def display_outro(self) -> None:
        """
        Displays the outro elements, including the "Thank You for Watching!" message
        and a subscribe prompt.

        Returns
        -------
        None
            This method does not return anything.
        """
        thank_you = Text(
            "Thank You for Watching!",
            font=DEFAULT_FONT,
            font_size=72,
            gradient=(YELLOW, ORANGE),
        ).shift(UP * 2)

        subscribe = Text(
            "Subscribe for more content!", font=DEFAULT_FONT, font_size=36, color=WHITE
        ).next_to(thank_you, DOWN)

        self.play(Write(thank_you), run_time=2)
        self.play(FadeIn(subscribe, shift=UP), run_time=1.5)
        self.wait(10)
        self.play(FadeOut(thank_you), FadeOut(subscribe), run_time=2.5)

    def construct(self) -> None:
        """
        Calls the display_outro method to construct the scene.

        Returns
        -------
        None
            This method does not return anything.
        """
        self.display_outro()
