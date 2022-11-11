"""——————————————————————
    Clase para inputs
——————————————————————"""


class Helpers:

    def __init__(self):
        pass

    @staticmethod
    def read_int(Message, error, min, max):
        while True:
            try:
                value = int(input(Message))
                if value < min or value > max:
                    raise
                else:
                    break
            except:
                print(error)
        return value

    @staticmethod
    def read_bolean(Message, error):
        while True:
            try:
                value = str(input(Message)).lower()
                if value.startswith('s') or value.startswith('y'):
                    value = True
                    break
                elif value.startswith('n'):
                    value = False
                    break
                else:
                    raise
            except:
                print(error)
        return value

    @staticmethod
    def get_color(color, intensity):
        if color == 'white':
            return (255, 255, 255)
        elif color == 'black':
            return (0, 0, 0)

        colors_tag = [['slate', 'gray', 'zinc', 'neutral', 'stone', 'red', 'pink', 'purple', 'deep-purple', 'indigo', 'blue', 'light-blue',
                       'cyan', 'teal', 'emerald', 'green', 'light-green', 'lime', 'yellow', 'amber', 'orange', 'deep-orange', 'brown'],
                      [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]]
        color_ref = [
            [(248, 250, 252), (241, 245, 249), (226, 232, 240), (203, 213, 225), (148, 163, 184), (100, 116, 139), (71, 85, 105), (51, 65, 85), (30, 41, 59), (15, 23, 42)     ],
            [(249, 250, 251), (243, 244, 246), (229, 231, 235), (209, 213, 219), (156, 163, 175), (107, 114, 128), (75, 85, 99), (55, 65, 81), (31, 41, 55), (17, 24, 39),     ],
            [(250, 250, 250), (244, 244, 245), (228, 228, 231), (212, 212, 216), (161, 161, 170), (113, 113, 122), (82, 82, 91), (63, 63, 70), (39, 39, 42), (24, 24, 27),     ],
            [(250, 250, 248), (245, 245, 245), (229, 229, 229), (212, 212, 212), (163, 163, 163), (115, 115, 115), (82, 82, 82), (64, 64, 64), (38, 38, 38), (23, 23, 23),     ],
            [(250, 250, 249), (245, 245, 244), (231, 229, 228), (214, 211, 209), (168, 162, 158), (120, 113, 108), (87, 83, 78), (68, 64, 60), (41, 37, 36), (28, 25, 23),     ],
            [(255, 235, 238), (255, 205, 210), (239, 154, 154), (229, 115, 115), (239, 83, 80), (244, 67, 54), (229, 57, 53), (211, 47, 47), (198, 40, 40), (183, 28, 28),     ],
            [(252, 228, 236), (248, 187, 208), (244, 143, 177), (240, 98, 146), (236, 64, 122), (233, 30, 99), (216, 27, 96), (194, 24, 91), (173, 20, 87), (136, 14, 79),     ],
            [(243, 229, 245), (225, 190, 231), (206, 147, 216), (186, 104, 200), (171, 71, 188), (156, 39, 176), (142, 36, 170), (123, 31, 162), (106, 27, 154), (74, 20, 140),],
            [(237, 231, 246), (209, 196, 233), (179, 157, 219), (149, 117, 205), (126, 87, 194), (103, 58, 183), (94, 53, 177), (81, 45, 168), (69, 39, 160), (49, 27, 146),   ],
            [(232, 234, 246), (197, 202, 233), (159, 168, 218), (121, 134, 203), (92, 107, 192), (63, 81, 181), (57, 73, 171), (48, 63, 159), (40, 53, 147), (26, 35, 126),    ],
            [(227, 242, 253), (187, 222, 251), (144, 202, 249), (100, 181, 246), (66, 165, 245), (33, 150, 243), (30, 136, 229), (25, 118, 210), (21, 101, 192), (13, 71, 161),],
            [(225, 245, 254), (179, 229, 252), (129, 212, 250), (79, 195, 247), (41, 182, 246), (3, 169, 244), (3, 155, 229), (2, 136, 209), (2, 119, 189), (1, 87, 155),      ],
            [(224, 247, 250), (178, 235, 242), (128, 222, 234), (77, 208, 225), (38, 198, 218), (0, 188, 212), (0, 172, 193), (0, 151, 167), (0, 131, 143), (0, 96, 100),      ],
            [(224, 242, 241), (178, 223, 219), (128, 203, 196), (77, 182, 172), (38, 166, 154), (0, 150, 136), (0, 137, 123), (0, 121, 107), (0, 105, 92), (0, 77, 64),        ],
            [(236, 253, 245), (209, 250, 229), (167, 243, 208), (110, 231, 183), (52, 211, 153), (16, 185, 129), (5, 150, 105), (4, 120, 87), (6, 95, 70), (6, 78, 59),        ],
            [(232, 245, 233), (200, 230, 201), (165, 214, 167), (129, 199, 132), (102, 187, 106), (76, 175, 80), (67, 160, 71), (56, 142, 60), (46, 125, 50), (27, 94, 32),    ],
            [(241, 248, 233), (220, 237, 200), (197, 225, 165), (174, 213, 129), (156, 204, 101), (139, 195, 74), (124, 179, 66), (104, 159, 56), (85, 139, 47), (51, 105, 30),],
            [(249, 251, 231), (240, 244, 195), (230, 238, 156), (220, 231, 117), (212, 225, 87), (205, 220, 57), (192, 202, 51), (175, 180, 43), (158, 157, 36), (130, 119, 23)],
            [(255, 253, 231), (255, 249, 196), (255, 245, 157), (255, 241, 118), (255, 238, 88), (255, 235, 59), (253, 216, 53), (251, 192, 45), (249, 168, 37), (245, 127, 23)],
            [(255, 248, 225), (255, 236, 179), (255, 224, 130), (255, 213, 79), (255, 202, 40), (255, 193, 7), (255, 179, 0), (255, 160, 0), (255, 143, 0), (255, 111, 0),     ],
            [(255, 243, 224), (255, 224, 178), (255, 204, 128), (255, 183, 77), (255, 167, 38), (255, 152, 0), (251, 140, 0), (245, 124, 0), (239, 108, 0), (230, 81, 0),      ],
            [(251, 233, 231), (255, 204, 188), (255, 171, 145), (255, 138, 101), (255, 112, 67), (255, 87, 34), (244, 81, 30), (230, 74, 25), (216, 67, 21), (191, 54, 12),    ],
            [(239, 235, 233), (215, 204, 200), (188, 170, 164), (161, 136, 127), (141, 110, 99), (121, 85, 72), (109, 76, 65), (93, 64, 55), (78, 52, 46), (62, 39, 35),       ]
        ]

        tag = [colors_tag[0].index(color), colors_tag[1].index(intensity)]
        return color_ref[tag[0]][tag[1]]

    # def draw_rounded_rect(self, surface, rect, color, corner_radius):
    #     ''' Draw a rectangle with rounded corners.
    #     Would prefer this:
    #         pygame.draw.rect(surface, color, rect, border_radius=corner_radius)
    #     but this option is not yet supported in my version of pygame so do it ourselves.

    #     We use anti-aliased circles to make the corners smoother
    #     '''
    #     if rect.width < 2 * corner_radius or rect.height < 2 * corner_radius:
    #         raise ValueError(
    #             f"Both height (rect.height) and width (rect.width) must be > 2 * corner radius ({corner_radius})")

    #     # need to use anti aliasing circle drawing routines to smooth the corners
    #     pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius, color)
    #     pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.top + corner_radius, corner_radius,
    #                             color)
    #     pygame.gfxdraw.aacircle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1, corner_radius,
    #                             color)
    #     pygame.gfxdraw.aacircle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1,
    #                             corner_radius, color)

    #     pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.top + corner_radius, corner_radius,
    #                                  color)
    #     pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.top + corner_radius,
    #                                  corner_radius, color)
    #     pygame.gfxdraw.filled_circle(surface, rect.left + corner_radius, rect.bottom - corner_radius - 1,
    #                                  corner_radius, color)
    #     pygame.gfxdraw.filled_circle(surface, rect.right - corner_radius - 1, rect.bottom - corner_radius - 1,
    #                                  corner_radius, color)

    #     rect_tmp = pygame.Rect(rect)

    #     rect_tmp.width -= 2 * corner_radius
    #     rect_tmp.center = rect.center
    #     pygame.draw.rect(surface, color, rect_tmp)

    #     rect_tmp.width = rect.width
    #     rect_tmp.height -= 2 * corner_radius
    #     rect_tmp.center = rect.center
    #     pygame.draw.rect(surface, color, rect_tmp)
