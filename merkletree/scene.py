from manim import *





class SimpleMerkleTree(Scene):
    def construct(self):

        # dots= Group(Dot().set_color(RED),Dot().move_to(LEFT),Dot().move_to(LEFT*2),Dot().move_to(LEFT*3),Dot().move_to(LEFT*4),Dot().move_to(RIGHT),Dot().move_to(RIGHT*2),Dot().move_to(RIGHT*3),Dot().move_to(RIGHT*4))
        # self.add(dots.move_to(UP))
        time = 1;
        scale= .8;
        ben=Tex(
            "",
            "\\texttt{\"less\"}",
            "",
            "",
            "",
            ""
        )

        hash_ben = Tex(
            "hash(",
            "\\texttt{\"less\"}",
            ")",
            "",
            "",
            ""
        )

        hash_ben_result = Tex(
            "hash(",
            "\\texttt{\"less\"}",
            ")",
            " = ",
            "\\texttt{0x7ba}"
            "\\texttt{5a7ff}..."
        )

        just_hash =  Tex(
            "",
            "",
            "",
            "",
            "\\texttt{0x7ba}"
            "\\texttt{5a7ff}..."
        )

        short_hash = Tex(
            "",
            "",
            "",
            "",
            "\\texttt{0x7ba}"
            "..."
        )


        self.play(Write(ben))
        self.wait(time)
        self.play(
            TransformMatchingTex(ben, hash_ben)
        )
        self.wait(time)
        self.play(
            TransformMatchingTex(hash_ben, hash_ben_result)
        )

        self.wait(time)
        self.play(TransformMatchingTex(hash_ben_result, just_hash))
        self.wait(time)
        self.play(FadeTransformPieces(just_hash, short_hash))
        first_hex = Tex("\\texttt{0x7ba}...").move_to(LEFT*3)
        self.play(ReplacementTransform(short_hash, first_hex))


        other_first_plain = Tex("\\texttt{\"trust\"}").move_to(LEFT)
        other_first_hex = Tex("\\texttt{0x8c4}...").move_to(LEFT)
        other_first_hash = MathTex("B_{hash}").move_to(LEFT)

        other_second_plain = Tex("\\texttt{\"more\"}").move_to(RIGHT)
        other_second_hex = Tex("\\texttt{0x650}...").move_to(RIGHT)
        other_second_hash = MathTex("C_{hash}").move_to(RIGHT)

        other_third_plain = Tex("\\texttt{\"truth\"}").move_to(RIGHT*3)
        other_third_hex = Tex("\\texttt{0x7a6}...").move_to(RIGHT*3)
        other_third_hash = MathTex("D_{hash}").move_to(RIGHT*3)

        plain_group = Group(other_first_plain, other_second_plain,other_third_plain)

        hex_group = Group(other_first_hex, other_second_hex,other_third_hex)


        self.play(FadeIn(plain_group))
        self.wait(time)
        self.play(ReplacementTransform(plain_group, hex_group))
        self.wait()
        hex_group = Group(first_hex, other_first_hex, other_second_hex,other_third_hex)


        first_hash = MathTex("A_{hash}").move_to(LEFT*3)
        hash_group = Group(first_hash,other_first_hash, other_second_hash,other_third_hash)
        self.play(ReplacementTransform(hex_group, hash_group))

        self.wait(time)
        self.play(hash_group.animate.shift(DOWN*2))

        combined_hash_one = MathTex("hash(A_{hash} + B_{hash})").move_to(LEFT*2).scale(scale)
        hash1_arrow = Arrow(first_hash.get_top(), combined_hash_one.get_bottom(), buff=0.25,stroke_width=3, max_tip_length_to_length_ratio=0.15)
        hash2_arrow = Arrow(other_first_hash.get_top(), combined_hash_one.get_bottom(), buff=0.25,stroke_width=3, max_tip_length_to_length_ratio=0.15)

        self.play(FadeIn(Group(combined_hash_one, hash1_arrow, hash2_arrow)))
        self.wait(time)

        combined_hash_two = MathTex("hash(C_{hash} + D_{hash})").move_to(RIGHT*2).scale(scale)
        hash1_arrow = Arrow(other_second_hash.get_top(), combined_hash_two.get_bottom(), buff=0.25, stroke_width=3, max_tip_length_to_length_ratio=0.15)
        hash2_arrow = Arrow(other_third_hash.get_top(), combined_hash_two.get_bottom(), buff=0.25,stroke_width=3, max_tip_length_to_length_ratio=0.15)

        self.play(FadeIn(Group(combined_hash_two, hash1_arrow, hash2_arrow)))
        self.wait(time)

        root_hash = MathTex("hash(hash(A_{hash} + B_{hash}) + hash(C_{hash} + D_{hash}))").move_to(UP*2).scale(scale)
        hash1_arrow = Arrow(combined_hash_one.get_top(), root_hash.get_bottom(), buff=0.25,stroke_width=3, max_tip_length_to_length_ratio=0.1)
        hash2_arrow = Arrow(combined_hash_two.get_top(), root_hash.get_bottom(), buff=0.25,stroke_width=3, max_tip_length_to_length_ratio=0.1)

        self.play(FadeIn(Group(root_hash, hash1_arrow, hash2_arrow)))
        self.wait(time)
        state_root = Tex("Merkle Root").move_to(UP*2)
        self.play(ReplacementTransform(root_hash, state_root))
        self.wait(time)
