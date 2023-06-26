from manim import *

class Fibonacci(Scene):
    def construct(self):

        init_pos = [-6, 0, 0]
        num_f = 10
        dist = 3
        
        arrow = []
        f = []
        num = [MathTex("0,").move_to(init_pos)]

        for i in range(num_f-1):
            num.append(MathTex(f"{fibonacci(i)},").next_to(num[i], RIGHT*dist))
        num.append(Text(". . .").next_to(num[-1], RIGHT*dist*0.8))

        for i in range(num_f):
            arrow.append(Arrow(buff=0.6, start=DOWN, end=UP, color=GRAY_A).next_to(num[i], DOWN))
            f.append(MathTex(f"F_{i}", color=GRAY_A).next_to(arrow[i], DOWN))

        txt = Text("La sucesión de Fibonacci", slant=ITALIC).scale(0.9).set_color_by_gradient(PURPLE, GOLD_D, PURPLE)

        self.play(Write(txt))
        self.play(txt.animate.shift(UP*3))
        self.play(*[Write(num[o]) for o in range(2)], run_time=2)
        self.play(
            *[Write(arrow[o]) for o in range(2)],
            *[Write(f[o]) for o in range(2)],
            run_time=1
            )
        for i in range(2,num_f):
            self.play(
            FadeIn(num[i], shift=RIGHT),
            FadeIn(arrow[i], shift=RIGHT),
            FadeIn(f[i], shift=RIGHT),
            run_time=((i-5.5)**2 + 3) / (20),
            )
            self.wait(0)
        
        self.play(FadeIn(num[-1], shift=RIGHT))
        
        fib = VGroup(
            *[num[o] for o in range(num_f+1)],
            *[arrow[o] for o in range(num_f)],
            *[f[o] for o in range(num_f)],
            )
        
        self.play(fib.animate.shift(UP*1.5), run_time=2)

        ecuation = MathTex("F_n=F_{n-1}+F_{n-2}").shift(DOWN*1.5).set_color_by_gradient(PURPLE, GOLD_D, PURPLE)
    
        self.play(Transform(txt, ecuation), run_time=2)
        self.wait()


def fibonacci(t):
    F = [0, 1]  # num es la lista donde se crea la sucesión
    #  F[0]=0, F[1]=1, ... F[i] = F[i-1] + F[i+1]

    # Se crea la sucesión
    for i in range(2,t+2): F.append(F[i-1] + F[i-2])
    print(F)
    return F[-1]