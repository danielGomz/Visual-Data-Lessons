from manim import *


class IntroScene(Scene):
    def construct(self):
        # Texto principal
        title = Text("Visual Data Lessons", font_size=72, gradient=(BLUE, GREEN))
        # Texto secundario
        subtitle = Text("Python, Data Science & More", font_size=36).next_to(title, DOWN)

        # Animación de entrada
        self.play(Write(title), run_time=2)
        self.play(FadeIn(subtitle, shift=UP), run_time=1.5)

        # Animación de salida
        self.wait(2)
        self.play(FadeOut(title), FadeOut(subtitle))
