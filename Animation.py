"""
This video includes content from the 2021 AP® Calculus AB Free-Response Questions,
© 2021 College Board. Used with permission.
"""

from manim import *
from manim.utils.rate_functions import ease_in_out_sine

class Animation(ThreeDScene):
    def construct(self):
        # * Functions
        def func(x):
            if x < 0 or x > 2:
                return 0

            return x * np.sqrt(4 - x**2)

        # * Parametric functions
        def func_x(t):
            return -2 * np.cos(t)

        def func_y(t):
            return -2 * np.sin(2 * t)

        # * Intro ==============================================================================================================
        intro_line1 = Tex(r"\text{AP Calculus AB}", font_size=24, color=WHITE)
        intro_line2 = Tex(
            r"\text{2021 FRQ - Question 3}", font_size=18, color=WHITE)
        intro_line3 = Tex(r"\text{Ben K}", font_size=12, color=WHITE)
        intro_group = VGroup(intro_line1, intro_line2, intro_line3).arrange(
            DOWN, center=True).move_to(ORIGIN)

        self.play(Write(intro_group), run_time=2.5)
        self.wait(1.0)
        self.play(FadeOut(intro_group), run_time=1)
        self.wait(0.5)

        # * Problem ============================================================================================================
        axes = ThreeDAxes(
            x_range=[0, 2.2, 0.5],
            y_range=[0, 2.2, 0.5],
            z_range=[-2.2, 2.2, 0.5],
            x_length=8,
            y_length=2.5,
            z_length=8,
            tips=False,
            stroke_width=2,
        )
        axes.z_axis.set_opacity(0)

        # * Add x/y labels to axis
        axes.add(
            MathTex("x").next_to(
                axes.x_axis.get_end(), RIGHT, buff=0.4),
            MathTex("y").next_to(
                axes.y_axis.get_end(), UP, buff=0.4)
        )
        axes.scale(0.3)

        graph = axes.plot_parametric_curve(
            lambda t: (func_x(t), func_y(t), 0),
            t_range=[PI / 2, PI],
            color=PINK,
            stroke_width=2,
        ).set_z_index(1)

        general_problem = Tex((
            r"A company designs spinning toys using the family of functions "
            r"$y = c x \sqrt{4 - x^2}$ where $c$ is a positive constant. "
            r"The figure below shows the region in the first quadrant bounded by the $x$-axis "
            r"and the graph of $y = c x \sqrt{4 - x^2}$, for some $c$. Each spinning toy is in the shape "
            r"of the solid generated when such a region is revolved about the $x$-axis. "
            r"Both $x$ and $y$ are measured in inches."
        ), font_size=10, tex_environment="flushleft").shift(UP * 0.6)
        graph_group = VGroup(graph, axes).shift(DOWN * 0.7)

        self.play(Write(general_problem), run_time=6)
        self.wait(0.25)
        self.play(Create(axes), run_time=1.5)

        axes.set_z_index(2)
        self.wait(0.25)
        self.play(Create(graph), run_time=2)
        self.wait(3)
        self.play(general_problem.animate.scale(0.7).shift(LEFT * 0.8).shift(UP * 0.2),
                  graph_group.animate.scale(0.5).shift(UP * 1.2).shift(RIGHT * 1.15), run_time=2)

        # * Problem Part A =======================================================================================================
        problem_a = Tex((
            r"(a) Find the area of the region in the first quadrant bounded by "
            r"the $x$-axis and the graph of $y = c x \sqrt{4 - x^2}$ for $c = 6$."
        ), font_size=8, tex_environment="center").shift(UP * 0.35)

        self.play(Write(problem_a), run_time=3)
        self.wait(0.5)

        x_tracker_a1 = ValueTracker(PI / 2)

        def get_parametric_area():
            t_vals = np.linspace(PI / 2, x_tracker_a1.get_value(), 100)
            points = [axes.c2p(func_x(t), func_y(t), 0) for t in t_vals]
            points.insert(0, axes.c2p(func_x(t_vals[0]), 0, 0))
            points.append(axes.c2p(func_x(t_vals[-1]), 0, 0))
            return Polygon(*points, color=BLUE, fill_opacity=0.5, stroke_width=0)

        area = always_redraw(get_parametric_area).set_z_index(-1)
        self.add(area)
        self.play(x_tracker_a1.animate.set_value(PI),
                  run_time=3, rate_func=ease_in_out_sine)
        self.wait(2)

        integral_definition = Tex((r"Since we know that the area under a curve $f$ is $\int_a^b f(x) dx$, we can find the area of the region by plugging in the given function:"),
                                  font_size=8, tex_environment="center")
        integral_definition_2 = Tex((r"$A = \int_a^b cx\sqrt{4 - x^2} dx$"), font_size=8,
                                    tex_environment="center").next_to(integral_definition, DOWN).shift(UP * 0.175)
        self.play(Write(integral_definition), run_time=3)
        self.play(Write(integral_definition_2), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(integral_definition), run_time=1)

        parta_area_1 = Tex((r"Given that $c = 6$, we can now plug in c into our integral:"),
                           font_size=8, tex_environment="center")
        parta_area_2 = Tex((r"$A = \int_a^b 6x\sqrt{4 - x^2} dx$"), font_size=8,
                           tex_environment="center").next_to(parta_area_1, DOWN).shift(UP * 0.112)
        parta_area_3 = Tex(
            (r"To find the endpoints of the integral, we can set the equation $y = 6x\sqrt{4 - x^2}$ equal to 0 and solve for $x$:"), font_size=8, tex_environment="center").shift(DOWN * 0.1)
        parta_area_4 = Tex(
            (r"$6x\sqrt{4 - x^2} = 0$"), font_size=8, tex_environment="center").shift(DOWN * 0.3)
        parta_area_5 = Tex(
            (r"$x\sqrt{4 - x^2} = 0$"), font_size=8, tex_environment="center").shift(DOWN * 0.3)
        parta_area_6 = Tex((r"$x = 0$"), font_size=8, tex_environment="center").shift(
            DOWN * 0.5).shift(LEFT * 0.25)
        parta_area_7 = Tex((r"$0 = \sqrt{4 - x^2}$"), font_size=8,
                           tex_environment="center").shift(DOWN * 0.495).shift(RIGHT * 0.15)
        parta_area_8 = Tex((r"$0 = 4 - x^2$"), font_size=8,
                           tex_environment="center").shift(DOWN * 0.495).shift(RIGHT * 0.15)
        parta_area_9 = Tex((r"$x^2 = 4$"), font_size=8, tex_environment="center").shift(
            DOWN * 0.495).shift(RIGHT * 0.15)
        parta_area_10 = Tex((r"$x = \pm2$"), font_size=8, tex_environment="center").shift(
            DOWN * 0.495).shift(RIGHT * 0.15)
        parta_area_11 = Tex((r"Since length can't be negative, 2 has to be positive"),
                            font_size=8, tex_environment="center").shift(DOWN * 0.66)
        parta_area_12 = Tex((r"$x = 2$"), font_size=8, tex_environment="center").shift(
            DOWN * 0.495).shift(RIGHT * 0.15)
        parta_area_13 = Tex((r"Thus, the lower and upper bounds of the integral are $0$ and $2$ respectively."),
                            font_size=8, tex_environment="center").shift(DOWN * 0.75)
        parta_area_14 = Tex((r"$A = \int_0^2 6x\sqrt{4 - x^2} dx$"), font_size=8,
                            tex_environment="center").shift(UP * 0.114)
        parta_area_14tip = Tex((r"We will need to use u-sub to solve this integral!"),
                               font_size=6, tex_environment="center").shift(RIGHT * 1.1).shift(DOWN * 0.095)
        parta_area_15 = Tex((r"Let $u = 4 - x^2$"), font_size=8,
                            tex_environment="center").shift(DOWN * 0.08)
        parta_area_16 = Tex((r"$du = -2x dx$"), font_size=8,
                            tex_environment="center").shift(DOWN * 0.21)
        parta_area_17 = Tex((r"$-\frac{1}{2}du = x dx$"), font_size=8,
                            tex_environment="center").shift(DOWN * 0.34)
        parta_area_18tip = Tex((r"Remember to change the limits of integration!"),
                               font_size=6, tex_environment="center").shift(RIGHT * 1.15).shift(DOWN * 0.512)
        parta_area_18 = Tex((r"$x = 0 \Rightarrow u = 4 - 0^2 = 4$"), font_size=8,
                            tex_environment="center").shift(DOWN * 0.45)
        parta_area_19 = Tex((r"$x = 2 \Rightarrow u = 4 - 2^2 = 0$"), font_size=8,
                            tex_environment="center").shift(DOWN * 0.55)
        parta_area_20 = Tex((r"$A = \int_4^0 6\left(-\frac{1}{2}\sqrt{u}\right) du$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_21 = Tex((r"$A = -3\int_4^0 \sqrt{u} du$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_22 = Tex((r"$A = 3\int_0^4 \sqrt{u} du$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_23 = Tex((r"$A = 2u^{\frac{3}{2}}\bigg \rvert^{u = 4}_{u = 0}$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_24 = Tex((r"$A = 2(4)^{\frac{3}{2}} - 2(0)^{\frac{3}{2}}$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_25 = Tex((r"$A = 2(8) - 0$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_26 = Tex((r"$A = 16$"), font_size=8,
                            tex_environment="center").shift(UP * 0.115)
        parta_area_27_final = Tex((r"$\therefore \text{The area of the region is } 16 \text{ square inches.}$"),
                                  font_size=8, tex_environment="center").shift(DOWN * 0.2)
        parta_area_27_final_tip = Tex((r"Remember to add units!"), font_size=6,
                                      tex_environment="center").shift(DOWN * 0.45)
        parta_area_27_final_box = SurroundingRectangle(
            parta_area_27_final, color=WHITE, stroke_width=1, buff=0.1)

        self.play(Write(parta_area_1), run_time=2)
        self.play(FadeTransform(integral_definition_2, parta_area_2), run_time=1)
        self.wait(2)
        self.play(FadeOut(parta_area_1),
                  parta_area_2.animate.shift(UP * 0.35), run_time=1)
        self.play(Write(parta_area_3), run_time=3)
        self.wait(0.1)
        self.play(Write(parta_area_4), run_time=1.5)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_4, parta_area_5), run_time=1)
        self.play(FadeIn(parta_area_6), FadeIn(parta_area_7), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_7, parta_area_8), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_8, parta_area_9), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_9, parta_area_10), run_time=1)
        self.wait(0.5)
        self.play(Write(parta_area_11), run_time=1.5)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_10, parta_area_12), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(parta_area_11), run_time=1)
        self.play(Write(parta_area_13), run_time=2)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_2, parta_area_14), run_time=0.5)
        self.wait(0.25)
        self.play(FadeOut(parta_area_13), FadeOut(parta_area_3), FadeOut(
            parta_area_5), FadeOut(parta_area_6), FadeOut(parta_area_12), run_time=0.5)
        self.wait(0.5)
        self.play(Write(parta_area_15), FadeIn(parta_area_14tip), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(parta_area_14tip), run_time=1)
        self.wait(0.5)
        self.play(Write(parta_area_16), run_time=1)
        self.wait(0.5)
        self.play(Write(parta_area_17), run_time=1)
        self.wait(0.5)
        self.play(Write(parta_area_18), Write(parta_area_19),
                  FadeIn(parta_area_18tip), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_14, parta_area_20), run_time=1)
        self.wait(0.5)
        self.play(FadeOut(parta_area_15), FadeOut(parta_area_16), FadeOut(parta_area_17),
                  FadeOut(parta_area_18), FadeOut(parta_area_18tip), FadeOut(parta_area_19), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_20, parta_area_21), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_21, parta_area_22), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_22, parta_area_23), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_23, parta_area_24), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_24, parta_area_25), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(parta_area_25, parta_area_26), run_time=1)
        self.wait(0.5)
        self.play(Write(parta_area_27_final), run_time=1)
        self.play(Create(parta_area_27_final_box), run_time=1)
        self.wait(0.25)
        self.play(FadeIn(parta_area_27_final_tip), run_time=1.5)
        self.wait(2)

        # * Problem Part B =======================================================================================================
        self.play(FadeOut(problem_a), FadeOut(parta_area_26), FadeOut(parta_area_27_final),
                  FadeOut(parta_area_27_final_box), FadeOut(parta_area_27_final_tip), FadeOut(area), FadeOut(x_tracker_a1), run_time=1)
        self.wait(0.5)

        problem_b = Tex((
            r"(b) It is known that, for $y=cx\sqrt{4-x^2}$, $\frac{dy}{dx} = \frac{c\left(4-2x^2\right)}{\sqrt{4-x^2}}$. "
            r"For a particular spinning toy, the radius of the largest cross-sectional circular slice is $1.2$ inches. "
            r"What is the value of $c$ for this spinning toy?"
        ), font_size=8, tex_environment="center").shift(UP * 0.35)

        x_tracker_b1 = ValueTracker(0)

        partb_dot = always_redraw(lambda: Dot(axes.c2p(x_tracker_b1.get_value(), func(
            x_tracker_b1.get_value())), radius=0.025, color=BLUE))

        self.play(Write(problem_b), run_time=3.5)
        self.wait(0.5)
        partb_dot.set_z_index(3)

        partb_ddx_1 = Tex((r"The cross-sectional circular slice with the largest radius "
                           r"occurs where $cx\sqrt{4 - x^2}$ has its maximum on the interval $0 < x < 2$."), font_size=8, tex_environment="center").shift(DOWN * 0.05)
        partb_ddx_2 = Tex((r"To find the maximum, we can set the derivative equal to $0$ and solve for $x$:"),
                          font_size=8, tex_environment="center").shift(DOWN * 0.24)
        partb_ddx_3 = Tex((r"$\frac{dy}{dx} = \frac{c\left(4-2x^2\right)}{\sqrt{4-x^2}} = 0$"), font_size=8,
                          tex_environment="center").shift(DOWN * 0.45)
        partb_ddx_3_tip = Tex((r"Remember to set the derivative equal to $0$!"),
                              font_size=6, tex_environment="center").shift(RIGHT * 1.1).shift(DOWN * 0.46)
        partb_ddx_4 = Tex((r"$c\left(4-2x^2\right) = 0$"),
                          font_size=8, tex_environment="center").shift(DOWN * 0.45)
        partb_ddx_5 = Tex((r"$c = 0$"), font_size=8, tex_environment="center").shift(
            LEFT * 0.25).shift(DOWN * 0.618)
        partb_ddx_6 = Tex((r"$4-2x^2 = 0$"), font_size=8,
                          tex_environment="center").shift(RIGHT * 0.15).shift(DOWN * 0.61)
        partb_ddx_7 = Tex((r"$2x^2 = 4$"), font_size=8, tex_environment="center").shift(
            RIGHT * 0.15).shift(DOWN * 0.61)
        partb_ddx_8 = Tex((r"$x^2 = 2$"), font_size=8, tex_environment="center").shift(
            RIGHT * 0.15).shift(DOWN * 0.61)
        partb_ddx_9 = Tex((r"$x = \pm\sqrt{2}$"), font_size=8, tex_environment="center").shift(
            RIGHT * 0.15).shift(DOWN * 0.61)
        partb_ddx_9_tip = Tex((r"Since length can't be negative, $\sqrt{2}$ has to be positive."),
                              font_size=8, tex_environment="center").shift(DOWN * 0.8)
        partb_ddx_10 = Tex((r"$x = \sqrt{2}$"), font_size=8, tex_environment="center").shift(
            RIGHT * 0.15).shift(DOWN * 0.61)
        partb_ddx_11 = Tex((r"Now that we've found $x$, we can solve for $c$ given that the radius is $1.2$ inches."),
                           font_size=8, tex_environment="center").shift(DOWN * 0.8)
        partb_ddx_12 = Tex((r"$1.2 = cx\sqrt{4 - x^2}$"),
                           font_size=8, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_13 = Tex((r"$1.2 = c\sqrt{2}\sqrt{4 - \sqrt{2}^2}$"),
                           font_size=6, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_14 = Tex((r"$1.2 = c\sqrt{2}\sqrt{4 - 2}$"),
                           font_size=8, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_15 = Tex((r"$1.2 = c\sqrt{2}\sqrt{2}$"),
                           font_size=8, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_16 = Tex((r"$1.2 = 2c$"),
                           font_size=9, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_17 = Tex((r"$c = 0.6$"),
                           font_size=9, tex_environment="center").shift(DOWN * 0.1)
        partb_ddx_17_final = Tex((r"$\therefore \text{The value of } c \text{ is } 0.6 \text{.}$"),
                                 font_size=8, tex_environment="center").shift(DOWN * 0.35)
        partb_ddx_17_final_box = SurroundingRectangle(
            partb_ddx_17_final, color=WHITE, stroke_width=1, buff=0.1)

        self.play(Write(partb_ddx_1), run_time=3)
        self.play(FadeIn(partb_dot), run_time=0.5)
        self.play(x_tracker_b1.animate.set_value(1.41421),
                  run_time=3, rate_func=ease_in_out_sine)
        self.wait(1)
        self.play(Write(partb_ddx_2), run_time=2)
        self.wait(0.5)
        self.play(Write(partb_ddx_3), run_time=2)
        self.play(FadeIn(partb_ddx_3_tip), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_3, partb_ddx_4),
                  FadeOut(partb_ddx_3_tip), run_time=1)
        self.wait(0.5)
        self.play(FadeIn(partb_ddx_5), FadeIn(partb_ddx_6), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_6, partb_ddx_7), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_7, partb_ddx_8), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_8, partb_ddx_9), run_time=1)
        self.wait(0.5)
        self.play(Write(partb_ddx_9_tip), run_time=2)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_9, partb_ddx_10),
                  FadeOut(partb_ddx_9_tip), run_time=1)
        self.wait(0.5)
        self.play(Write(partb_ddx_11), run_time=2)
        self.wait(1)
        self.play(FadeOut(partb_ddx_1), FadeOut(partb_ddx_2), FadeOut(partb_ddx_4), FadeOut(
            partb_ddx_5), FadeOut(partb_ddx_11), partb_ddx_10.animate.move_to(ORIGIN).shift(DOWN * 0.3), FadeIn(partb_ddx_12), run_time=1)
        self.wait(1)
        self.play(FadeTransform(
            VGroup(partb_ddx_10, partb_ddx_12), partb_ddx_13), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_13, partb_ddx_14), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_14, partb_ddx_15), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_15, partb_ddx_16), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partb_ddx_16, partb_ddx_17), run_time=1)
        self.wait(0.5)
        self.play(Write(partb_ddx_17_final), run_time=1)
        self.play(Create(partb_ddx_17_final_box), run_time=1)
        self.wait(2)

        # * Problem Part C =======================================================================================================
        self.play(FadeOut(problem_b), FadeOut(partb_dot), FadeOut(partb_ddx_17), FadeOut(
            partb_ddx_17_final), FadeOut(partb_ddx_17_final_box), run_time=1)
        self.wait(0.5)

        new_axes = ThreeDAxes(
            x_range=[0, 2.2, 0.5],
            y_range=[-2.2, 2.2, 0.5],
            z_range=[-2.2, 2.2, 0.5],
            x_length=8,
            y_length=5,
            z_length=8,
            tips=False
        )
        new_axes.add(
            MathTex("x").next_to(
                new_axes.x_axis.get_end(), RIGHT, buff=0.4).scale(1.1),
            MathTex("y").next_to(
                new_axes.y_axis.get_end(), UP, buff=0.4).scale(1.1),
            MathTex("z").next_to(
                new_axes.z_axis.get_end(), OUT, buff=0.4).scale(1.1),
        )

        new_axes.scale(0.15)

        problem_c = Tex((
            r"(c) For another spinning toy, the volume is $2\pi$ cubic inches. What is the value of $c$ for this spinning toy?"
        ), font_size=8, tex_environment="center").shift(UP * 0.3)

        self.play(Write(problem_c), run_time=3)
        self.wait(0.5)

        self.add_fixed_in_frame_mobjects(
            general_problem, problem_c)

        e = ValueTracker(0)
        surface = always_redraw(
            lambda: Surface(
                lambda u, v: new_axes.c2p(
                    func_x(u),
                    func_y(u) * np.cos(v),
                    func_y(u) * np.sin(v)
                ),
                u_range=[PI / 2, PI],
                v_range=[0, e.get_value()],
                checkerboard_colors=[GREEN, PURPLE],
                fill_opacity=0.5,
            )
        )

        n_slices = 1000
        slices = VGroup()
        for i in range(n_slices):
            x = (i + 0.5) * 2 / n_slices
            radius = func(x)
            if radius == 0:
                continue

            p0 = new_axes.c2p(x, 0, 0)
            p1 = new_axes.c2p(x, radius, 0)
            scaled_radius = np.linalg.norm(p1 - p0)

            disk = Circle(radius=scaled_radius, color=RED,
                          fill_opacity=0.005, stroke_opacity=0.0)
            disk.rotate(PI / 2, axis=UP)
            disk.move_to(new_axes.c2p(x, 0, 0))
            slices.add(disk)

        slices.set_z_index(3)

        new_graph = new_axes.plot_parametric_curve(
            lambda t: (func_x(t), func_y(t), 0),
            t_range=[PI / 2, PI],
            color=PINK,
            stroke_width=2,
        ).set_z_index(1)

        VGroup(new_axes, new_graph, slices).shift(DOWN * 0.9)

        self.play(graph_group.animate.move_to(ORIGIN).scale(
            1.1).shift(DOWN * 0.3).shift(RIGHT * 0.2), run_time=2.5)

        self.play(FadeOut(graph), run_time=1)
        self.play(Transform(axes, new_axes), run_time=1.5)
        self.play(Create(new_graph), run_time=2)
        self.add(surface)
        self.move_camera(
            phi=45 * DEGREES,
            theta=-130 * DEGREES,
            gamma=-50 * DEGREES,
            run_time=3,
            rate_func=ease_in_out_sine,
        )
        self.play(
            LaggedStart(*[Create(b)
                          for b in slices], lag_ratio=0.05),
            run_time=6,
            rate_func=ease_in_out_sine,
        )
        self.wait(2)
        self.play(
            Rotating(new_graph, axis=RIGHT, radians=TAU,
                     about_point=new_axes.c2p(0, 0, 0)),
            e.animate.set_value(2 * PI),
            run_time=6,
            rate_func=ease_in_out_sine,
        )
        self.wait(2)
        self.move_camera(
            phi=0 * DEGREES,
            theta=-90 * DEGREES,
            gamma=0 * DEGREES,
            run_time=3,
            rate_func=ease_in_out_sine,
            added_anims=[
                *[disk.animate.set_fill(opacity=0.05) for disk in slices]]
        )
        self.remove(axes, new_graph)
        self.play(VGroup(new_axes, slices).animate.scale(
            0.7).shift(UP * 1.35).shift(RIGHT * 1.2), run_time=2)
        self.wait(1)

        partc_volume_1 = Tex((r"Given that the function is revolved around the x axis, we can use "
                              r"the equation $\int_a^b \pi f(x)^2 dx$ to find the volume of the solid."),
                             font_size=8, tex_environment="center").shift(UP * 0.05)
        partc_volume_1_tip = Tex((r"Remember that the area of a circle is $\pi r^2$!"),
                                 font_size=6, tex_environment="flushleft").shift(RIGHT * 1.2).shift(DOWN * 0.35)
        partc_volume_1_tip2 = Tex((r"Remember to square the function!"),
                                  font_size=6, tex_environment="flushleft").shift(RIGHT * 1.2).shift(DOWN * 0.45)
        partc_volume_2 = Tex((r"After substituting our function into the equation, we get:"),
                             font_size=8, tex_environment="center").shift(DOWN * 0.15)
        partc_volume_3 = Tex((r"$V = \int_0^2 \pi \left(cx\sqrt{4 - x^2}\right)^2 dx$"), font_size=8,
                             tex_environment="center").shift(DOWN * 0.35)
        partc_volume_4 = Tex((r"$V = \pi c^2 \int_0^2 x^2(4 - x^2) dx$"), font_size=8,
                             tex_environment="center").shift(DOWN * 0.0)
        partc_volume_5 = Tex((r"$V = \pi c^2 \int_0^2 (4x^2 - x^4) dx$"), font_size=8,
                             tex_environment="center").shift(DOWN * 0.0)
        partc_volume_6 = Tex((r"$V = \pi c^2 \left(\frac{4x^3}{3} - \frac{x^5}{5}\right) \bigg \rvert^{x = 2}_{x = 0}$"),
                             font_size=8, tex_environment="center").shift(DOWN * 0.0)
        partc_volume_7 = Tex((r"$V = \pi c^2 \left(\frac{4(2)^3}{3} - \frac{(2)^5}{5} - \left(\frac{4(0)^3}{3} - \frac{(0)^5}{5}\right)\right)$"),
                             font_size=8, tex_environment="center").shift(DOWN * 0.0)
        partc_volume_8 = Tex((r"$V = \pi c^2 \left(\frac{32}{3} - \frac{32}{5}\right)$"),
                             font_size=8, tex_environment="center").shift(DOWN * 0.0)
        partc_volume_9 = Tex((r"$V = \frac{64\pi c^2}{15}$"),
                             font_size=8, tex_environment="center").shift(DOWN * 0.0)
        partc_volume_10 = Tex((r"Since we know that the volume is $2\pi$, we can set the equation equal to $2\pi$ and solve for $c$."), font_size=8,
                              tex_environment="center").shift(DOWN * 0.25)
        partc_volume_11 = Tex((r"$\frac{64\pi c^2}{15} = 2\pi$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_12 = Tex((r"$\frac{64c^2}{15} = 2$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_13 = Tex((r"$64c^2 = 30$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_14 = Tex((r"$c^2 = \frac{30}{64}$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_15 = Tex((r"$c = \sqrt{\frac{30}{64}}$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_16 = Tex((r"$c = \sqrt{\frac{15}{32}}$"), font_size=8,
                              tex_environment="center").shift(DOWN * 0.0)
        partc_volume_17_final = Tex((r"$\therefore \text{When the volume is } 2\pi \text{ cubic inches, the value of } c \text{ is } \sqrt{\frac{15}{32}}\text{.}$"),
                                    font_size=8, tex_environment="center").shift(DOWN * 0.4)
        partc_volume_17_final_box = SurroundingRectangle(
            partc_volume_17_final, color=WHITE, stroke_width=1, buff=0.1)

        self.play(Write(partc_volume_1), run_time=3)
        self.wait(1)
        self.play(Write(partc_volume_2), run_time=2)
        self.wait(0.25)
        self.play(Write(partc_volume_3), FadeIn(partc_volume_1_tip),
                  FadeIn(partc_volume_1_tip2), run_time=2)
        self.wait(1)
        self.play(FadeOut(partc_volume_2), FadeOut(partc_volume_1_tip),
                  FadeOut(partc_volume_1_tip2), FadeOut(partc_volume_1), run_time=1)
        self.wait(0.5)
        self.play(partc_volume_3.animate.shift(UP * 0.35), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_3, partc_volume_4),
                  FadeOut(partc_volume_3), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_4, partc_volume_5),
                  FadeOut(partc_volume_4), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_5, partc_volume_6),
                  FadeOut(partc_volume_5), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_6, partc_volume_7),
                  FadeOut(partc_volume_6), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_7, partc_volume_8),
                  FadeOut(partc_volume_7), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_8, partc_volume_9),
                  FadeOut(partc_volume_8), run_time=1)
        self.wait(0.5)
        self.play(Write(partc_volume_10), run_time=3)
        self.wait(2)
        self.play(FadeTransform(partc_volume_9, partc_volume_11),
                  FadeOut(partc_volume_10), FadeOut(partc_volume_9))
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_11, partc_volume_12),
                  FadeOut(partc_volume_11), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_12, partc_volume_13),
                  FadeOut(partc_volume_12), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_13, partc_volume_14),
                  FadeOut(partc_volume_13), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_14, partc_volume_15),
                  FadeOut(partc_volume_14), run_time=1)
        self.wait(0.5)
        self.play(FadeTransform(partc_volume_15, partc_volume_16),
                  FadeOut(partc_volume_15), run_time=1)
        self.wait(0.5)
        self.play(Write(partc_volume_17_final), run_time=1)
        self.play(Create(partc_volume_17_final_box), run_time=1)
        self.wait(2)
