from manim import *


class Pythagorean(Scene):

    # main
    def construct(self):

        # +-- VARIABLES --+#
    
        # la posición del "triángulo de referencia", trg
        trg_x, trg_y = -6, 1

        # la posición de los triángulos del que partirán otros, el primero (otf_1) y el segundo (otf_2)
        oft_1x, oft_1y = -1, -1
        oft_2x, oft_2y = -3, -1

        # los colores de los cuadrados, el primero (c_sqr1), el segundo (c_sqr2) y el tercero (c_sqr3)
        c_sqr1 = RED
        c_sqr2 = GREEN
        c_sqr3 = BLUE

        # +---------------+#

        # --- #

        # +-- Presentación --+#

        # se crean los textos, el primero en prsnt, y el segundo en dmt
        prsnt = Text("El Teorema de Pitágoras",
                     font_size=45).set_color_by_gradient(PURPLE, GOLD)
        dmt = Text("Una demostración sin palabras",
                   font_size=30).set_color_by_gradient(GOLD, PURPLE)

        # se dibuja el texto prsnt en pantalla
        self.play(Write(prsnt), run_time=2.5)
        # se transforma en el texto dmt
        self.play(Transform(prsnt, dmt), run_time=2.5)
        self.play(FadeOut(prsnt), run_time=2)   # el texto se desvanece
        self.wait(0.5)

        # +------------------+#

        # --- #

        # +-- Primera sección --+#

        # se crea el triángulo de referencia, trg, y otros 4 con la función get_trg()
        trg, trg_1, trg_2, trg_3, trg_4 = [
            get_trg(trg_x, trg_y) for _ in range(5)]

        # se crean las etiquetas de los lados del triángulo trg con la función get_lab_trg()
        l_trg = get_lab_trg(trg)

        # se dibuja el triángulo trg con sus etiquetas
        self.play(Write(trg), run_time=1.5)
        self.play(Write(l_trg))
        self.wait(0.75)

        # se dibuja al resto de triángulos y se anima cómo se mueven y ...
        # ... colocan uno detrás del otro con la función move_trg()
        self.add(trg_1, trg_2, trg_3, trg_4)
        self.play(
            *[move_trg(trg_1, trg_2, trg_3, trg_4, oft_1x, oft_1y)[o] for o in range(0, 4)]
        )

        # se anima su rotación y movimiento para que formen el primer cuadrado, c^2
        self.play(
            trg_2.animate.move_to(
                [oft_1x+1.5, oft_1y-0.5, 0]).rotate(PI/2),  # -1.5, -1.5
            trg_3.animate.move_to(
                [oft_1x+2, oft_1y+1, 0]).rotate(PI),  # -1, 0
            trg_4.animate.move_to(
                [oft_1x+0.5, oft_1y+1.5, 0]).rotate(3*PI/2),  # -2.5, 0.5
            run_time=1.5
        )

        # se crean las etiquetas de cada uno de los triángulos
        l_trg_1 = get_lab_trg(trg_1)
        l_trg_2 = get_lab_trg(trg_2, c=UP)
        l_trg_3 = get_lab_trg(trg_3, c=LEFT)
        l_trg_4 = get_lab_trg(trg_4, c=DOWN)

        # se dibuja en pantalla
        self.play(
            *[Write(o)
              for o in [l_trg_1[2], l_trg_2[2], l_trg_3[2], l_trg_4[2]]],
            run_time=2
        )

        # se obtiene la mitad de la base, m1, y de la altura, m2, del cuadrado formado por los triángulos
        m1 = mid(trg_1[0].get_right(), trg_2[0].get_right())
        m2 = mid(trg_3[0].get_right(), trg_2[0].get_right()) + \
            0.5  # + 0.5 por el superíndice 2

        # se crea el texto "c^2" en el medio del cuadrado
        cdr_c = MathTex("c^2").move_to([m1[0], m2[1], 0])

        # se anima la transformación de los "c" al "c^2"
        self.play(
            *[ReplacementTransform(o, cdr_c)
              for o in [l_trg_1[2], l_trg_2[2], l_trg_3[2], l_trg_4[2]]]
        )
        self.wait(0.5)
        self.play(Flash(cdr_c, flash_radius=0.4, color=c_sqr1),
                  run_time=0.75)  # se anima un destello
        self.wait(0.5)

        # se crea el cuadrado c^2 que forman los triángulos con la función get_plg() [ver línea 335]
        sqr_c = get_plg(
            trg_1[1].get_right(),
            trg_2[1].get_top(),
            trg_3[1].get_left(),
            trg_4[1].get_bottom(),
            c_sqr1
        )

        # más animaciones!
        self.play(
            Create(sqr_c),   # dibuja el cuadrado c^2 en la pantalla
            # colorea la hipotenusa del triángulo trg
            trg[2].animate.set_color(c_sqr1),
            # colorea la etiqueta de la hipotenusa de trg
            l_trg[2].animate.set_color(c_sqr1),
            cdr_c.animate.set_color(c_sqr1)  # colorea el "c^2"
        )
        self.play(
            sqr_c.animate.set_fill(),   # rellena el cuadrado
            cdr_c.animate.set_z_index(1),   # trae al frente el "c^2"
            run_time=0.25
        )
        self.play(
            sqr_c.animate.set_fill(BLACK),  # rellena el cuadrado de negro
            run_time=0.4
        )
        self.wait()

        # se crea un grupo grp_sqr_c en el que se contiene toda la figura
        grp_sqr_c = VGroup(trg_1, trg_2, trg_3, trg_4, cdr_c, sqr_c)

        # +-------------------+#

        # --- #

        # +-- Segunda sección --+#

        # se crean otros cuatro triángulos
        trg_5, trg_6, trg_7, trg_8 = [get_trg(-6, 1) for _ in range(4)]

        self.play(
            # se mueve a la figura anterior a la derecha
            grp_sqr_c.animate.shift(RIGHT*3.5),
            # se anima cómo se mueven y colocan los nuevos triángulos uno detrás del otro
            *[move_trg(trg_5, trg_6, trg_7, trg_8, oft_2x, oft_2y)[o] for o in range(0, 4)]
        )

        # se anima cómo se mueven y rotan para formar dos cuadrados, a^2 y b^2
        self.play(
            trg_5.animate.move_to([-3, 0, 0]),
            trg_6.animate.move_to([-3, 0, 0]).rotate(PI),
            trg_7.animate.move_to([-1.5, -1.5, 0]).rotate(-PI/2),
            trg_8.animate.move_to([-1.5, -1.5, 0]).rotate(PI/2),
            run_time=1.5
        )
        self.wait()

        # se crean las etiquetas de los triángulos
        l_trg_5 = get_lab_trg(trg_5, b=DOWN*0.45)
        l_trg_6 = get_lab_trg(trg_6, a=RIGHT)
        l_trg_7 = get_lab_trg(trg_7, a=UP, b=LEFT*0.45)

        # se dibujan sus etiquetas en pantalla
        self.play(
            *[Write(o)
              for o in [l_trg_5[1], l_trg_6[0], l_trg_7[0], l_trg_7[1]]],
            run_time=2
        )

        # se obtiene la mitad de la base, m1, y de la altura, m2, del cuadrado a^2
        m1 = mid(trg_8[0].get_left(), trg_8[0].get_right())
        m2 = mid(trg_5[0].get_left(), trg_5[0].get_right())

        # se obtiene la mitad de la base, m1, y de la altura, m2, del cuadrado b^2
        m3 = mid(trg_5[1].get_left(), trg_5[1].get_right())
        m4 = mid(trg_8[1].get_left(), trg_8[1].get_right())

        # se crean los textos "a^2" y "b^2", cada uno en la mitad del cuadrado que le corresponde
        cdr_a = MathTex("a^2").move_to([m1[0], m2[1], 0])
        cdr_b = MathTex("b^2").move_to([m3[0], m4[1], 0])

        # se anima la transformación de los "a" y los "b" a los "a^2" y "b^2"
        self.play(
            ReplacementTransform(l_trg_6[0], cdr_a),
            ReplacementTransform(l_trg_7[0], cdr_a),
            ReplacementTransform(l_trg_5[1], cdr_b),
            ReplacementTransform(l_trg_7[1], cdr_b)
        )
        self.wait(0.5)
        self.play(
            # se anima un destello para "a^2"
            Flash(cdr_a, flash_radius=0.4, color=c_sqr2),
            # se anima un destello para "b^2"
            Flash(cdr_b, flash_radius=0.4, color=c_sqr3),
            run_time=0.75
        )
        self.wait(0.5)

        # se crea el cuadrado a^2 formado por los triángulos
        sqr_a = get_plg(
            trg_7[0].get_left(),
            trg_7[0].get_right(),
            trg_7[0].get_right() + (0, 2, 0),
            trg_6[0].get_top(),
            c_sqr2
        )

        # se crea el cuadrado b^2 formado por los triángulos
        sqr_b = get_plg(
            trg_8[0].get_left() - (1, 0, 0),
            trg_7[1].get_bottom(),
            trg_5[1].get_right(),
            trg_5[1].get_left(),
            c_sqr3
        )

        self.play(
            Create(sqr_a),  # se dibuja el cuadrado a^2
            Create(sqr_b),  # se dibuja el cuadrado b^2
            trg[0].animate.set_color(c_sqr2),  # colorea el cateto a de trg
            trg[1].animate.set_color(c_sqr3),  # colorea el cateto b de trg
            # colorea la etiqueta del cateto a
            l_trg[0].animate.set_color(c_sqr2),
            # colorea la etiqueta del cateto b
            l_trg[1].animate.set_color(c_sqr3),
            cdr_a.animate.set_color(c_sqr2),  # colorea el "a^2"
            cdr_b.animate.set_color(c_sqr3)  # colorea el "b^2"
        )
        self.play(
            sqr_a.animate.set_fill(),  # rellena el cuadrado a^2
            cdr_a.animate.set_z_index(1),  # trae al frente el "a^2"
            sqr_b.animate.set_fill(),  # rellena el cuadrado b^2
            cdr_b.animate.set_z_index(1),  # trae al frente el "b^2"
            run_time=0.25
        )
        self.play(
            # rellena el el cuadrado a^2 de negro
            sqr_a.animate.set_fill(BLACK),
            # rellena el el cuadrado b^2 de negro
            sqr_b.animate.set_fill(BLACK),
            run_time=0.4
        )
        self.wait()

        # se crea un grupo grp_sqr_a_b en el que se contiene toda la figura
        grp_sqr_a_b = VGroup(trg_5, trg_6, trg_7, trg_8,
                             cdr_a, sqr_a, cdr_b, sqr_b)

        # +--------------------+#

        # --- #

        # +-- The End --+#

        # se se anima cómo se mueven ambas figuras hacia arriba
        self.play(
            grp_sqr_c.animate.shift(UP*2),
            grp_sqr_a_b.animate.shift(UP*2)
        )

        # se crea el texto prff "a^2 + b^2 = c^2"
        prff = MathTex("a^2", "+", "b^2", "=",
                       "c^2").set_color_by_gradient(c_sqr2, c_sqr3, c_sqr1)

        # se transforma el "a^2", el "b^2" y el "c^2" en su lugar del texto prff
        self.play(
            TransformMatchingShapes(cdr_a, prff[0]),
            TransformMatchingShapes(cdr_b, prff[2]),
            TransformMatchingShapes(cdr_c, prff[4]),
            # se desvanece la figura del grupo grp_sqr_c
            FadeOut(grp_sqr_c - cdr_c),
            # se desvanece la figura del grupo grp_sqr_a_b
            FadeOut(grp_sqr_a_b - cdr_a - cdr_b),
            FadeOut(trg, l_trg),  # se desvanece trg con sus etiquetas
            run_time=4
        )
        # se dibujan en pantalla los signos que faltaban del texto prff
        self.play(
            Write(prff[1]),
            Write(prff[3]),
            run_time=3
        )
        # se crea el rectángulo donde se va a contener la fórmula
        box = SurroundingRectangle(prff, color=PURPLE, buff=0.3)
        # se dibuja el rectángulo en pantalla
        self.play(Write(box), run_time=2)
        # se desvanece el texto prff y el rectángulo
        self.play(FadeOut(prff, box), run_time=4)

        # +-------------+#


#    ____________
#   /_._._._._._.\
#  /_._._._._._._.\
#   |   ___    __|
#   |   |_|    | |
#  _|__________|_|__
#  |...............|
# _|...functions...|_
# /...................\

# crea un triángulo rectángulo
def get_trg(a, b):

    # B
    # | \
    # |  \
    # A---C

    dot = [
        [a, b, 0],   # Dot A = [a, b], dot[0]
        [a, b + 2, 0],   # Dot B, dot[1]
        [a + 1, b, 0]   # Dot C, dot[2]
    ]

    cat_a = Line(dot[0], dot[1])
    cat_b = Line(dot[0], dot[2])
    hip = Line(dot[1], dot[2])

    return VGroup(cat_a, cat_b, hip)

# --- #

# crea las etiquetas de los tres lados de un triángulo
def get_lab_trg(trg, a=LEFT, b=DOWN, c=RIGHT):
    l_a = MathTex("a", color=trg[0].get_color()).next_to(trg[0], a)
    l_b = MathTex("b", color=trg[1].get_color()).next_to(trg[1], b)
    l_hip = MathTex("c", color=trg[2].get_color()).move_to(trg[2], c)

    return VGroup(l_a, l_b, l_hip)

# --- #

# crea la animación de los triángulos colocándose uno detrás del otro
def move_trg(trg1, trg2, trg3, trg4, a, b):
    t1 = trg1.animate.move_to([a, b, 0])
    t2 = trg2.animate.move_to([a+1, b, 0])
    t3 = trg3.animate.move_to([a+2, b, 0])
    t4 = trg4.animate.move_to([a+3, b, 0])
    return t1, t2, t3, t4

# --- #

# crea un cuadrado
def get_plg(a, b, c, d, clr):
    plg = Polygon(
        a, b, c, d,
        color=clr,
        fill_color=clr,
        fill_opacity=0.3
    )
    return plg
