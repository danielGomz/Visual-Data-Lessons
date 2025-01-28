from manim import *


class OutroScene(Scene):
    def construct(self):
        thank_you = Text("Thank You for Watching!", font_size=72, gradient=(YELLOW, ORANGE))
        subscribe = Text("Subscribe for more content!", font_size=36).next_to(thank_you, DOWN)

        self.play(Write(thank_you), run_time=2)
        self.play(FadeIn(subscribe, shift=UP), run_time=1.5)
        self.play(Create(icons), run_time=2)

        self.wait(2)
        self.play(FadeOut(thank_you), FadeOut(subscribe), FadeOut(icons))
