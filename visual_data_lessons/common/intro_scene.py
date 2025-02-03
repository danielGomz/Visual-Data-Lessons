from manim import BLUE, BOLD, DOWN, GREEN, UL, UP, FadeIn, FadeOut, Scene, Text, Transform, Write

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

    def display_intro(self, video_title: str = None, author_name: str = "Daniel Gómez") -> None:
        """
        Displays the channel name and description, then optionally transforms the channel name into the video title.

        Parameters
        ----------
        video_title : str, optional
            The title of the video to display. If None, only the channel name and description are shown.
            Default is None.
        author_name : str, optional
            The name of the author or presenter to display. Default is "Daniel Gómez".

        Returns
        -------
        None
            This method does not return anything.

        Notes
        -----
        If a video title is provided, the channel name will be replaced with the video title after the description is displayed.
        """
        project_name = Text(
            "Visual Data Lessons",
            font=DEFAULT_FONT,
            font_size=72,
            gradient=(GREEN, BLUE),
            weight=BOLD,
        )

        host_text = Text(
            f"Presented by {author_name}", font=DEFAULT_FONT, font_size=36, weight="LIGHT"
        ).next_to(project_name, DOWN)

        self.play(Write(project_name))
        self.play(FadeIn(host_text, shift=UP), run_time=1.5)

        self.wait(1)
        self.play(FadeOut(host_text))

        if video_title is not None:
            title_text = Text(
                video_title,
                font=DEFAULT_FONT,
                font_size=72,
                weight=BOLD,
            )

            self.play(Transform(project_name, title_text))

            self.play(project_name.animate.scale(0.3).to_edge(UL))

            self.play(FadeOut(project_name))

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
        self.display_intro(video_title="Video Title")
