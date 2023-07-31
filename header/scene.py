from manim import *


# \begin{table}[]
# \begin{tabular}{|l|l|l|l|}
# \hline
# a & b & c & d \\ \hline
# \end{tabular}
# \end{table}
class MyScene(Scene):
    def construct(self):

        time_factor = 1
        scale_factor = .8
        table = Tex("""
                    \\begin{table}[]
                    \\begin{tabular}{|l|l|l|l|}
                    \\hline
                    a & b & c & d \\\\ \\hline
                    \\end{tabular}
                    \\end{table}
                    """
                    )

        next_table = Tex("""
                    \\begin{table}[]
                    \\begin{tabular}{|l|l|l|l|}
                    \\hline
                    d & c & b & a \\\\ \\hline
                    \\end{tabular}
                    \\end{table}
                    """
                    )

        self.play(Write(table))
        self.wait(time_factor)
        self.play(TransformMatchingShapes(table,next_table))
        self.wait(time_factor)
