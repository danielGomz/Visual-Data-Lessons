from manim import (
    BLUE,
    BOLD,
    DOWN,
    GREEN,
    LEFT,
    UL,
    UP,
    FadeIn,
    FadeOut,
    Scene,
    Text,
    Transform,
    Write,
)

from visual_data_lessons.config import DEFAULT_FONT


class IntroScene(Scene):
    """
    A scene for introducing a video with the channel name, description, and the title of the video.

    This scene displays the channel name, a brief description, and optionally transforms the channel name into the video title.

    Methods
    -------
    display_intro(title_video: str = None) -> None
        Displays the channel name, description, and optionally the video title.
    construct() -> None
        Calls the display_intro method to construct the scene.
    """

    def display_intro(self, title_video: str = None) -> None:
        """
        Displays the channel name and description, then optionally transforms the channel name into the video title.

        Parameters
        ----------
        title_video : str, optional
            The title of the video to display. If None, only the channel name and description are shown.
            Default is None.

        Returns
        -------
        None
            This method does not return anything.

        Notes
        -----
        If a video title is provided, the channel name will be replaced with the video title after the description is displayed.
        """
        chanel_name = Text(
            "Visual Data Lessons",
            font=DEFAULT_FONT,
            font_size=72,
            gradient=(GREEN, BLUE),
            weight=BOLD,
        )

        description_text = Text(
            "Python, Data Science & More", font=DEFAULT_FONT, font_size=36, weight="LIGHT"
        ).next_to(chanel_name, DOWN)

        self.play(Write(chanel_name))
        self.play(FadeIn(description_text, shift=UP), run_time=1.5)

        self.wait(1)
        self.play(FadeOut(description_text))

        if title_video is not None:
            title_video_text = Text(
                title_video,
                font=DEFAULT_FONT,
                font_size=72,
                weight=BOLD,
            )

            self.play(Transform(chanel_name, title_video_text))

            self.play(
                chanel_name.animate.scale(0.3).move_to(
                    self.camera.frame_width * LEFT / 2 + self.camera.frame_height * UP / 2,
                    aligned_edge=UL,
                )
            )

            self.play(FadeOut(chanel_name))

        self.wait(1)

    def construct(self) -> None:
        """
        Calls the display_intro method to construct the scene with a sample video title.

        This method is automatically called by Manim to construct the scene.

        Returns
        -------
        None
            This method does not return anything.

        """
        self.display_intro(title_video="Video Title")
