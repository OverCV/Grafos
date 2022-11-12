"""————————————————————————————————————————————————————
    Manejo de operaciones sobre la interfaz gráfica
————————————————————————————————————————————————————"""
import os, sys, time, random

import pygame

from pygame.locals import *
from controles.helpers import Helpers
#! from data.Entity import *


class Interfaz:
    """—————————————————————————————————————————————CONSTRUCTOR——————————————————————————————————————————————————————"""

    def __init__(self, menu):
        pygame.font.init()

        self.menu = menu  # This activates the graph functionality in real time.

        self.size = (1280, 720)  # Screen resolution.
        self.panel = (0, 0)  # The main canvas for the simulation.
        self.grid = []  # All screen positions for all the nodes.
        self.divs = (12, 7)  # Screen divisions.

        self.colors = []    # List filled with Helpers colors.
        self.font_SCP = pygame.font.SysFont('Source Code Pro', 30)

        self.mp = [(0, 0), False]  # Mouse Position | (x, y), Clicked |
        self.FPS = 60  # FPS ratio.
        self.clock = pygame.time.Clock()

    """
    self.reach = [False, 0, 0]
    self.intersects = []
    self.path_vertex = []
    self.path_edges = []

    self.walker = Entity(30, 40, 0)
    self.LDM = False
    self.loaded_json = False
    """  # old attributes
    """
    def set_size(self):
        o = { 1: (720, 400), 2: (720, 576), 3: (1280, 720), 4: (1920, 1080),
              5: (2048, 1080), 6: (2560, 1440), 7: (3840, 2160) }
        i = Helpers.read_int('| [1] (720, 400) | [2] (720, 576) | [3] (1280, 720) '
                             '| [4] (1920, 1080) | [5] (2560, 1440) | [6] (3840, 2160) | [7] (3840, 2160) |\n',
                             '| Pantalla inválida |', 1, 7)
        self.size = o[i]
        print('Pantalla redimensionada.')
"""  # Set screen
    """
    def set_divs(self):
        infty = sys.maxsize
        x = Helpers.read_int('Ingrese las divisiones en [ x ]: ', 'Valor inválido.', 1, infty)
        y = Helpers.read_int('Ingrese las divisiones en [ y ]: ', 'Valor inválido.', 1, infty)

        self.divs = (x, y)
        print('Divisiones creadas.')
"""  # Set divs

    @staticmethod
    def draw_text(window: pygame.Surface, text: str, aa: bool, fg: tuple,
                  x: int | float, y: int | float, size: int) -> None:
        """
        Function to draw text on window.

        :param _window: window to draw text on (pygame.Surface)
        :param text: text to draw on window (str)
        :param font: font to render the text with (pygame.font.Font)
        :param aa: use antialiasing (bool)
        :param fg: foreground color (str)
        :param bg: background color (str)
        :param x: x coordinate of window to draw text on (int | float)
        :param y: y coordinate of window to draw text on (int | float)
        :param centered_x: center in the x-axis (bool)
        :param centered_y: center in the y-axis (bool)
        :return: None
        """

        font = pygame.font.SysFont('Consolas', size)
        text = font.render(text, aa, fg)  # Atributo: bg

        window.blit(text, (x, y))

    def draw_text_1(self, surface, text, color, font, x, y):
        txt_obj = font.render(text, color, 1)
        txt_rect = txt_obj.get_rect()
        txt_rect.topcenter = (x, y)
        surface.blit(txt_obj, txt_rect)

    # def draw_text(self, surface, text, size, pos):
    #     blue_900 = Helpers.get_color('blue', 900)
    #     font = pygame.font.SysFont('Consolas', size)
    #
    #     text_surface = font.render(text, True, blue_900)
    #
    #     surface.blit(text_surface, pos)

    """—————————————————————————————————————————————MÉTODOS——————————————————————————————————————————————————————————"""

    def main_menu(self):
        pygame.init()
        pygame.font.init()
        phi = 0.61803398875

        indigo_300 = Helpers.get_color('indigo', 300)

        logo = self.load_images()[0]
        colors = ['black', 'white', 'neutral', 'neutral', 'emerald', 'emerald', 'indigo', 'indigo', 'red', 'red']
        shades = [0, 0, 100, 200, 100, 300, 100, 300, 100, 300]
        if len(self.colors) == 0:
            for i in range(len(colors)):
                self.colors.append(Helpers.get_color(colors[i], shades[i]))

        self.panel = (self.size[0] * phi, self.size[1])  # Panel con dimensión en (x) de proporción aurea.

        self.grid.append(self.get_grid(self.size[0] * phi, self.size[1]))  # Editado para ver grafo en panel.

        # Ventana principal
        pygame.display.set_caption('Proyecto Grafos'),
        window = pygame.display.set_mode(self.size, pygame.RESIZABLE)
        panel = pygame.Rect(0, 0, self.panel[0], self.panel[1])

        self.draw_text(window, 'main menu', True, self.colors[0], 00, 00, 20)  # black.

        run = True
        while run:
            window.fill(self.colors[1])  # white.

            self.mp[0] = pygame.mouse.get_pos()
            self.mp[1] = pygame.mouse.get_pressed()[0]

            divs_x, divs_y = self.size[0] / 13, self.size[1] / 7
            x5, y9 = self.size[0] / 5, self.size[1] / 9

            window.blit(logo, ((4 * divs_x) - (x5 / 2), (divs_y) - (y9 / 2)))

            # Se busca dar ajuste a los botones del menú inicial, se itera la posición menos su longitud en (x, y).
            simulation_BTN = pygame.Rect((3 * divs_x) - (x5 / 2), (6 * divs_y) - (y9 / 2), x5,
                                         y9)  # left | top | width | height

            options_BTN = pygame.Rect((6 * divs_x) - (x5 / 2), (6 * divs_y) - (y9 / 2), x5,
                                      y9)  # left | top | width | height

            load_json_BTN = pygame.Rect((9 * divs_x) - (x5 / 2), (6 * divs_y) - (y9 / 2), x5,
                                        y9)  # left | top | width | height

            # sim =     # neutral_100
            # pygame.draw.rect(window, self.colors[2], simulation_BTN)
            Helpers.draw_rounded_rect(self, window, simulation_BTN, self.colors[2], 15)
            self.draw_text(window, 'Simulator', True, self.colors[0], 2 * divs_x, (6 * divs_y), 30)

            # opt =    # neutral_100
            # pygame.draw.rect(window, self.colors[2], options_BTN)
            Helpers.draw_rounded_rect(self, window, options_BTN, self.colors[2], 15)
            self.draw_text(window, 'Options', True, self.colors[0], 5 * divs_x, (6 * divs_y), 30)

            # json =  # neutral_100
            # pygame.draw.rect(window, self.colors[2], load_json_BTN)
            Helpers.draw_rounded_rect(self, window, load_json_BTN, self.colors[2], 15)
            self.draw_text(window, 'Load JSON', True, self.colors[0], 8 * divs_x, (6 * divs_y), 30)

            if simulation_BTN.collidepoint(self.mp[0]):  # Si está sobre simulator.
                # neutral_200
                # pygame.draw.rect(window, self.colors[3], simulation_BTN)
                Helpers.draw_rounded_rect(self, window, simulation_BTN, self.colors[3], 15)
                self.draw_text(window, 'Simulator', True, self.colors[0], 2 * divs_x, (6 * divs_y), 30)
                if self.mp[1]:  # Presiona clic.
                    self.simulator(window, panel)

            if options_BTN.collidepoint(self.mp[0]):  # Si está sobre options.
                # neutral_200
                # pygame.draw.rect(window, self.colors[3], options_BTN)
                Helpers.draw_rounded_rect(self, window, options_BTN, self.colors[3], 15)
                self.draw_text(window, 'Options', True, self.colors[0], 5 * divs_x, (6 * divs_y), 30)
                if self.mp[1]:  # Presiona click.
                    self.options(window)

            if load_json_BTN.collidepoint(self.mp[0]):  # Si está sobre load_json.
                # neutral_200
                # pygame.draw.rect(window, self.colors[3], load_json_BTN)
                Helpers.draw_rounded_rect(self, window, load_json_BTN, self.colors[3], 15)
                self.draw_text(window, 'Load JSON', True, self.colors[0], 8 * divs_x, (6 * divs_y), 30)
                if self.mp[1]:  # Presiona click.
                    self.load_json(window)

            pygame.display.update()
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == VIDEORESIZE:
                    w_h = (event.w, event.h)
                    window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.size = w_h
        pygame.quit()

    def simulator(self, window, panel):
        run = True
        while run:
            window.fill(self.colors[3])  # white

            self.draw_text(window, 'Simulator', True, self.colors[0], 20, 20, 30)

            pygame.display.update()
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                if event.type == VIDEORESIZE:
                    w_h = (event.w, event.h)
                    window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
                    self.size = w_h
        return

    # def options(self, window):
    #
    #     has_sounds = [1, 'Sonido: ONN']
    #     has_sfx = [1, 'SFX: ONN']
    #     toggle = ['ON', 'OFF']
    #     color = self.colors[2]
    #
    #     run = True
    #     while run:
    #         window.fill(self.colors[1])
    #
    #         left_panel = pygame.Rect(0, 0, window.get_width() / 5, window.get_height())  # left | top | width | height #
    #         pygame.draw.rect(window, self.colors[3], left_panel)
    #
    #         right_panel_center_x = (window.get_width() - (window.get_width() / 5)) / 2 + (window.get_width() / 5)
    #         pygame.draw.line(window, self.colors[2], (right_panel_center_x, 0),
    #                          (right_panel_center_x, window.get_height()))
    #
    #         rp_cx_left = 1 * (window.get_width() - (window.get_width() / 5)) / 4 + (
    #                     window.get_width() / 5)  # 1/4 de la columna.
    #         rp_cx_right = 3 * (window.get_width() - (window.get_width() / 5)) / 4 + (
    #                     window.get_width() / 5)  # 3/4 de la columna
    #
    #         # Linea verde, [5].
    #         pygame.draw.line(window, self.colors[4], (rp_cx_left, 0), (rp_cx_left, window.get_height()), 5)
    #         # Linea roja, [7].
    #         pygame.draw.line(window, self.colors[8], (rp_cx_right, 0), (rp_cx_right, window.get_height()), 5)
    #
    #         options_x = (window.get_width() / 10) - 80  # Posición - Dimensiones en x (Posibilidad sea doble de fuente).
    #         options_y = (window.get_height() / 2) - 20  # Posición - Dimensiones en y (fuente 40 -> 40/2).
    #         self.draw_text(window, 'Options', True, self.colors[0], options_x, options_y, 40)
    #
    #         # BOTONES #
    #         right_panel_divs_y = window.get_height() / 5
    #
    #         for i in range(5):
    #
    #             over_lp = (window.get_width() / 5) < self.mp[0][0] < right_panel_center_x
    #             over_rp = right_panel_center_x < self.mp[0][0] < window.get_width()
    #
    #             # Líneas negra[0].
    #             div_mid_y = (i + (1 / 2)) * (((i + 1) * right_panel_divs_y) - (i * right_panel_divs_y))
    #             pygame.draw.line(window, self.colors[0], (window.get_width() / 5, div_mid_y),
    #                              (window.get_width(), div_mid_y))
    #
    #             hx, hy = (window.get_width() - (window.get_width() / 5)) * 0.4, (window.get_height() / 6) * 0.6
    #             if i == 0:
    #                 over_module = 0.5 * div_mid_y < self.mp[0][1] < 1.5 * div_mid_y
    #                 # Rectángulos + Texto.
    #                 sound_BTN = pygame.Rect(rp_cx_left - hx / 2, div_mid_y - hy / 2, hx,
    #                                         hy)  # left | top | width | height #
    #                 sfx_BTN = pygame.Rect(rp_cx_right - hx / 2, div_mid_y - hy / 2, hx,
    #                                       hy)  # left | top | width | height #
    #
    #                 ## Dibujado sobre el panel derecho ##
    #                 pygame.draw.rect(window, color, sound_BTN)
    #                 if over_lp and over_module:
    #                     color = self.colors[3]
    #                     pygame.draw.rect(window, color, sound_BTN)
    #
    #                     if self.mp[1]:
    #                         self.mp[1] = False  # Cambiamos el atributo de clic a falso para que no quede infinito.
    #                         # Adición de switch para cambio de estado.
    #                         has_sounds[0] += (0.20)
    #                         if int(has_sounds[0]) % 2 == 0:
    #                             has_sounds[1] = 'Sonido: ' + toggle[0]
    #                             color = self.colors[4]  # green.
    #                         else:
    #                             has_sounds[1] = 'Sonido: ' + toggle[1]
    #                             color = self.colors[8]  # red.
    #                 self.draw_text(window, has_sounds[1], True, self.colors[0], rp_cx_left - hx / 4, div_mid_y - hy / 4,
    #                                30)
    #
    #                 ## Dibujado sobre el panel derecho ##
    #                 pygame.draw.rect(window, color, sfx_BTN)
    #                 if over_rp and over_module:
    #                     color = self.colors[3]
    #                     pygame.draw.rect(window, color, sfx_BTN)
    #
    #                     if over_rp and over_module:
    #                         color = self.colors[3]
    #                         pygame.draw.rect(window, color, sfx_BTN)
    #
    #                         if self.mp[1]:
    #                             self.mp[1] = False  # Cambiamos el atributo de clic a falso para que no quede infinito.
    #                             # Adición de switch para cambio de estado.
    #                             has_sfx[0] += (0.20)
    #                             if int(has_sfx[0]) % 2 == 0:
    #                                 has_sfx[1] = 'SFX: ' + toggle[0]
    #                                 color = self.colors[4]  # green.
    #                             else:
    #                                 has_sfx[1] = 'SFX: ' + toggle[1]
    #                                 color = self.colors[8]  # red.
    #                 self.draw_text(window, has_sfx[1], True, self.colors[0], rp_cx_right - hx / 4, div_mid_y - hy / 4,
    #                                30)
    #
    #                 # Si se modifica el atributo del texto en tamaño, ha de modificarse la diferencia en posición.
    #
    #             self.mp[0] = pygame.mouse.get_pos()  # Actualiza la posición del cursor.
    #             self.mp[1] = pygame.mouse.get_pressed()[0]  # Presiona el click izquierdo?
    #
    #             # pygame.draw.line(window, self.colors[2], (window.get_width()/5, i*right_panel_divs_y),
    #             #                  (window.get_width(), i*right_panel_divs_y))
    #
    #         # UPDATE + End of the function.
    #         pygame.display.update()
    #         self.clock.tick(self.FPS)
    #
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 run = False
    #             if event.type == KEYDOWN:
    #                 if event.key == K_ESCAPE:
    #                     run = False
    #             if event.type == VIDEORESIZE:
    #                 w_h = (event.w, event.h)
    #                 window = pygame.display.set_mode(w_h, pygame.RESIZABLE)
    #                 self.size = w_h
    #     return

    # def load_json(self, window):
    #     i = 3
    #     while True:
    #         window.fill(self.colors[1])
    #
    #         x, y = self.size[0] / 2, self.size[1] / 3
    #         txt = 'back in 0' + str(i) + ' ...'
    #         # self.draw_text(window, '', self.colors[8], self.font_SCP, 20, 20)
    #         self.draw_text(window, 'json loaded', True, self.colors[0], 20, 20, 30)
    #         self.draw_text(window, txt, True, self.colors[0], x, 2 * y, 30)
    #
    #         pygame.display.update()
    #         self.clock.tick(self.FPS)
    #
    #         # Tiempo de lectura.
    #         time.sleep(1)
    #         i -= 1
    #         if i == 0:
    #             break
    #     return

    def get_grid(self, w, h):
        div_x, div_y = self.divs[0], self.divs[1]
        # (w / div_x, h / div_y)
        plano = []  # Contiene los puntos (div_x[n], div_y[n]) en el plano para hacer las líneas (por ejemplo)

        # Al hacer que vaya desde (div_x - 1) o (div_y - 1) se elimina la posibilidad de elegir la última casilla borde.
        for i in range(div_x - 1):
            for j in range(div_y - 1):
                x = ((w / div_x) * (i + 1)).__round__(2)
                y = ((h / div_y) * (j + 1)).__round__(2)

                plano.append((x, y))
        return plano

        # Configuración inicial | Comentar o des-comentar según se desee
        # self.set_size()
        # self.set_divs()
        #
        # response = input('¿Bajos recursos? (LDM): ').lower()[0]
        # if response == 's':
        #     self.LDM = True
        #
        # response = input('¿Cargar JSON? (LDM): ').lower()[0]
        # if response == 's':
        #     self.loaded_json = True

    def interface(self, window, panel):
        # Imágenes
        # images = self.load_images()
        walker_move = pygame.sprite.Group()
        walker_move.add(self.walker)

        neutral_50 = Helpers.get_color('neutral', 50)
        zinc_200 = Helpers.get_color('zinc', 200)

        window.fill(neutral_50)

        # Este método tiene usabilidad en la selección de textos, al cliquearse activa el recorrido en mención.
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()

        # Hacemos obtención del recorrido (lista con vértices) para luego con el grid hacer la "animación".
        camino = self.create_modules(window, mouse_pos, mouse_click)

        # Primero dibujar los módulos y luego el panel (rectangular) de proporción aurea para el Grafo.
        pygame.draw.rect(window, Helpers.get_color('white', 0), panel)

        # El plano es la lista (Tuples) con posiciones para dar ubicación a los vértices.
        # grid = self.grid(window.get_width(), window.get_height()) # Original
        grid = self.grid(window.get_width() * 0.61803398875, window.get_height())  # Editado para ver grafo en panel.

        # Si no hay interseptos generados, lo hace.
        if len(self.intersects) == 0:
            # self.create_intersects(grid) # Función de uso único en la carga de interface.
            self.create_intersects_nice(grid)  # Función de uso único en la carga de interface.

        # CREACIÓN DE VÉRTICES Y ARISTAS #
        vertices = self.get_vertex(grid)
        self.draw_lines(window, vertices, grid, 0)

        if self.LDM:
            self.draw_circles(window, grid)
        else:
            self.draw_vertex(window, grid)  # Forma NO ÓPTIMA, ver si antes guardar esa lista y luego imprimir.

        # self.draw_all_circles(window, grid)
        # Tenemos el grid, hagamos lo propuesto 19 líneas antes.
        if camino:
            self.draw_lines(window, vertices, grid, 1)
            if self.LDM:
                self.draw_circles(window, grid)
            else:
                self.draw_vertex(window, grid)  # Forma NO ÓPTIMA, ver si antes guardar esa lista y luego imprimir.

            if mouse_click[0] and (self.reach[0] is False):
                # Hay camino, clic + Sin fin de recorrido
                self.animate_path(window, camino, vertices, grid)

        # Finalidad de cuando esté activo, se pueda repetir el ciclo para el recorrido de vértices.
        # Explicación: Desactivado por Default y ( !?! ), el objeto llega al final del recorrido, reach en i, j habrá de
        # tornarse a 0 para resetear el ciclo de iterators.
        # Reseteo de valores del walker, la idea es que se restablezca para el siguiente algoritmo.
        if (mouse_click[0] is False) and self.reach[0]:
            pos = self.search_casita(grid, vertices)
            self.walker.set_pos(pos)
            self.reach[0] = False
            self.reach[1] = 0
            self.reach[2] = 0
            self.path_vertex = []

        walker_move.draw(window)
        walker_move.update(0.1, 0)

        # ACCIÓN FINAL # Actualización de pantalla para cambio de frame.
        pygame.display.update()

    def search_casita(self, grid, vertices):
        vertex = self.menu.grafo.get_lista_vertices()

        for i in range(len(vertex)):
            if vertex[i].get_dato() == 'Casita':
                index = vertices[i][1]
                position = grid[index]
                break
        return position

    def create_modules(self, window, mouse_pos, clicked):
        """
        Crea las divisiones cuáles además de dar al usuario apoyo visual, determinan posiciones para las cuales
        el mouse identificará en (y) para dar coloreado.
        """
        # Inicialización de colores
        neutral_100 = Helpers.get_color('neutral', 100)
        neutral_200 = Helpers.get_color('neutral', 200)

        blue_100 = Helpers.get_color('blue', 100)
        indigo_100 = Helpers.get_color('indigo', 100)
        red_50 = Helpers.get_color('red', 50)
        indigo_300 = Helpers.get_color('indigo', 300)

        emerald_200 = Helpers.get_color('emerald', 200)

        div_y = self.size[1] / 11

        texts = ['Algoritmos', 'Prim', 'Dijkstra', 'Kruskal', 'Boruvka', 'Recorridos', 'Anchura', 'Profundidad',
                 'Floyd-Warshall', 'Ford-Fulkerson', 'Bloquear arista']

        conjunto_v = []
        conjunto_a = []

        for i in range(11):  # Este ciclo va desde 0 hasta 9
            panel = pygame.Rect(0, div_y * i, self.size[0], div_y)
            color = neutral_100

            mouse_over_x = mouse_pos[0] > (window.get_width() * 0.618)  # Un booleano auto-calculado. :0.
            mouse_over_y = div_y * i < mouse_pos[1] < div_y * (i + 1)
            over = False

            if mouse_over_x and mouse_over_y:
                over = True

            if i == 10 and over:
                color = red_50
                if clicked[0]:
                    # pygame.quit()
                    # self.sub_interface()
                    break

            else:
                if over:
                    color = neutral_200
                    if clicked[0]:
                        color = emerald_200

                if 0 < i < 5:
                    if over:
                        if clicked[0]:
                            conjunto_v = self.menu.algoritmo_i(i)[0]
                            conjunto_a = self.menu.algoritmo_i(i)[1]

                    pygame.draw.rect(window, color, panel)

                elif 5 < i < 10:
                    if over:
                        if clicked[0]:
                            conjunto_v = self.menu.algoritmo_i(i)[0]
                            conjunto_a = self.menu.algoritmo_i(i)[1]

                else:
                    color = indigo_100

            pygame.draw.rect(window, color, panel)

            # text_x = (self.size[0] * 0.618) + self.size[0] * 1
            text_x = ((self.size[0] * 1.618) / 2) - 100

            self.draw_text(window, texts[i], 20, (text_x, div_y * i + 20))

        # Base fundamental del método, con este retorno se obtiene la lista de vértices cuál habrá de recorrerse.
        self.path_edges = conjunto_a
        return conjunto_v

    def animate_path(self, window, path, v_pos, grid):

        v_i = self.reach[1]  # Obtención del índice para cuál será la arista inicial (sea path su iterando).
        v_list = self.menu.grafo.get_lista_vertices()

        if v_i == len(v_list) - 1:
            self.reach[0] = True
            print('| Last i index arrived! | reached = True | ')
            return

        # Solo por inicializar índices jsjs.
        index_o = index_d = (-1)

        # Obtención de los índices de los vértices dónde se hará recorrido de un extremo a otro. Esto con fin de conocer
        # en grid mediante el índice cuál es la coordenada a trabajar (x, y). Se recorre mediante el iterando
        # print(len(path))
        for j in range(len(v_list) - 1):
            # print(v_i+0, 'path[i+0]:', path[v_i + 0], '|', (v_i+1), ' path[i+1]:', path[v_i + 1],)
            # print('vértice_j:', v_pos[j])
            # if path[v_i+0] == v_list[j]:
            if path[v_i + 0] == v_list[j].get_dato():
                # print('i+0 encontrado')
                index_o = j
            # if path[v_i+1] == v_list[j]:
            if path[v_i + 1] == v_list[j].get_dato():
                # print('i+1 encontrado')
                index_d = j
            # Con esta condición decimos que pare de iterar entre los vértices y ahora tenemos un único índice, el
            # necesario para que este y su siguiente hagan la animación.

        # Dentro de la lista de posiciones por vértice se obtiene la posición dentro del grid
        origen = v_pos[index_o][1]
        destino = v_pos[index_d][1]

        # print('path to do:', path)
        # print('grid origin:', grid[origen], 'grid destiny:', grid[destino])
        self.animate_pair(window, path, grid[origen], grid[destino])  # Animación de la lista de pares tuples.

    def animate_pair(self, window, path, origen_g, destino_g):
        # VARIABLE GLOBAL REACH: Esta tendría un boolean y el índice de la arista, hasta que llegue se activa y pasa
        # para la siguiente posición que implica la siguiente arista del conjunto recorrido de aristas
        j = self.reach[2]
        # position = (10, 10)

        # Los parámetros se llaman x_g dado son tuples de los vértices de la rejilla (grid). (Grid)~(G rid)~(G).
        # player_sprite = self.load_images()[0]

        reached = self.reach[0]  # Boolean.

        # final_e_pos = self.order_vertices(origen_g, destino_g)
        e_Dx = (destino_g[0] - origen_g[0]) / 100
        e_Dy = (destino_g[1] - origen_g[1]) / 100

        px = py = (-1)
        if j <= 100:
            if j == 0:
                self.path_vertex.append(origen_g)  # Sea la j = 0, entonces adicionamos este grid para visualizarlo.

            px = ((j * e_Dx) + origen_g[0])
            py = ((j * e_Dy) + origen_g[1])
            position = (px, py)

            self.reach[2] += 5

            if j == 100:
                # Incremento de cada arista [i] en la lista camino.
                self.reach[1] += 1
                # Incremento de cada posición [j] para el update de pantalla.
                self.reach[2] = 0
                # Inserción de coordenada vértice al camino (way)
                self.path_vertex.append(destino_g)

        self.walker.set_pos(position)

        # Imagen | Posición : Patojito
        # window.blit(self.walker.image, self.walker.get_pos())

        # print('walker_pos:', self.walker.get_pos())

    def draw_lines(self, window, vertices, grid, id):

        indigo_100 = Helpers.get_color('indigo', 100)
        emerald_200 = Helpers.get_color('emerald', 200)
        color = indigo_100

        aristas = self.menu.grafo.get_lista_aristas()

        if id == 1:
            # self.draw_path
            aristas = self.path_edges
            color = emerald_200

        for arista in aristas:
            """
            Por cada arista, obtenemos el índice del vértice dónde origina, y el índice de dónde destina.
            Estos son los índices de los vértices origen y destino de la arista [i].
            """
            # Índices de los vértices. (Fin de las definiciones xd)
            origen_i = self.get_i_vertice(arista, 'origen')
            destino_i = self.get_i_vertice(arista, 'destino')

            # vert [(0, 14), (1, 15), (2, 18), ∙∙∙, (10, 64)] # Tantas posiciones como vértices existentes.
            # grid [(106.67, 102.86), (106.67, 205.71), ∙∙∙, (106.67, 308.57)] # Máximo de (divs_x * divs_y) posiciones.

            grid_x1 = grid[vertices[origen_i][1]][0]
            grid_y1 = grid[vertices[origen_i][1]][1]

            grid_x2 = grid[vertices[destino_i][1]][0]
            grid_y2 = grid[vertices[destino_i][1]][1]

            # Dibujado estándar de la línea.
            pygame.draw.line(window, color, (grid_x1, grid_y1), (grid_x2, grid_y2), 5)

            # Visualización de valor de la arista.
            self.draw_value(window, grid_x1, grid_y1, grid_x2, grid_y2, arista)

        return True

    def get_i_vertice(self, arista, lugar):
        vertices = self.menu.grafo.get_lista_vertices()

        if lugar == 'origen':
            for i in range(len(vertices)):
                if arista.get_origen() == vertices[i].get_dato():
                    return i
        else:
            for i in range(len(vertices)):
                if arista.get_destino() == vertices[i].get_dato():
                    return i

    def draw_value(self, window, x1, y1, x2, y2, arista):
        Dx = ((x2 + x1) / 2)
        Dy = ((y2 + y1) / 2)

        pos = (Dx, Dy)
        self.draw_text(window, str(arista.get_peso()), 20, pos)

    def draw_all_circles(self, window, grid):
        """
        Dibuja todos los vértices disponibles de la rejilla (grid) y de paso les imprime su índice.
        """
        indigo_100 = Helpers.get_color('indigo', 100)
        for i in range(len(grid)):
            pygame.draw.circle(window, indigo_100, (grid[i][0], grid[i][1]), (window.get_width() / len(grid)))
            self.draw_text(window, str(i), 20, (grid[i][0], grid[i][1]))

    def draw_circles(self, window, grid):
        """
        Método del cual a partir de un sistema de rejillas (grid) con posiciones (x, y) imprimirá los vértices a partir
        de los interseptos (intersects) cuáles son posiciones True en el (grid), con esto se conoce mediante una lista
        de vértices la posición del vértice impreso dentro de la lista de vértices y la posición dentro del grid para el
        cual se le dio ubicación.

        :param window: Es la ventana dónde se imprimirán los vértices.
        :param grid: Es el sistema de divisiones para dar ubicación a los vértices.
        :param self.intersects: Es el sistema posiciones disponibles para ubicar los vértices.
        :return: vertices. Lista con el índice del vértice en la lista grafo e índice cuál se le asigna en el grid.
        """
        indigo_300 = Helpers.get_color('indigo', 300)
        emerald_300 = Helpers.get_color('emerald', 300)
        v = self.menu.grafo.get_lista_vertices()

        # | vértice | x | y | #
        vertices = []
        j = 0
        # print('plane len - 1:', len(plane) - 1)
        # print('intersecciones:', self.intersects)

        for i in range(len(grid)):
            if self.intersects[i]:
                vertices.append((j, i))
                pygame.draw.circle(window, indigo_300, (grid[i][0], grid[i][1]), (window.get_width() / len(grid)))

                grid_pos_i = (grid[i][0], grid[i][1])
                # print('grid_i:', grid_pos_i, '| way:', self.way)
                if grid_pos_i in self.path_vertex:
                    pygame.draw.circle(window, emerald_300, grid_pos_i, (window.get_width() / len(grid)))

                pos = (grid[i][0] - 100, grid[i][1] + 20)
                self.draw_text(window, v[j].get_dato(), 20, pos)
                # self.draw_text(window, v[j].get_dato(), 20, (grid[i][0], grid[i][1]))
                j += 1

        return vertices

    def draw_vertex(self, window, grid):
        library_off = self.load_images()[0][0]
        library_on = self.load_images()[0][1]
        # emerald_300 = Helpers.get_color('emerald', 300)

        red_300 = Helpers.get_color('red', 300)
        list_vertex = self.menu.grafo.get_lista_vertices()
        j = 0

        for i in range(len(grid)):
            if self.intersects[i]:
                # pygame.draw.circle(window, emerald_300, (grid[i][0], grid[i][1]), (window.get_width() / len(grid)) )
                grid_pos_i = (grid[i][0], grid[i][1])

                window.blit(library_off, (grid[i][0] - (self.size[0] / 16), grid[i][1] - (self.size[1] / 12)))
                # print('grid_i:', grid_pos_i, '| way:', self.way)
                if grid_pos_i in self.path_vertex:
                    # pygame.draw.circle(window, red_300, grid_pos_i, (window.get_width() / len(grid)))
                    window.blit(library_on, (grid[i][0] - (self.size[0] / 10), grid[i][1] - (self.size[1] / 6)))

                pos = (grid[i][0] - 100, grid[i][1] + 20)
                self.draw_text(window, list_vertex[j].get_dato(), 20, pos)
                j += 1

    def get_vertex(self, grid):
        vertex = []
        j = 0

        for i in range(len(grid)):
            if self.intersects[i]:
                vertex.append((j, i))
                j += 1
        return vertex

    def create_intersects(self, grid):
        """
        Método cuál muta el atributo intersects con un grid alterno, este con posiciones True's o False's distribuidas
        al azar para cada una de las posiciones del grid, por ello está de parámetro.
        """
        for i in range(len(grid)):
            self.intersects.append(False)

        # En este método hasta que no se llenen con True's random los huecos, no retornará un (True) el método.
        while not self.count_intersects():
            r = random.randint(0, len(grid) - 1)
            # No podemos volver doblemente (True) una posición.
            if self.intersects[r] is False:
                # print('Intersepto', self.spaces[i], 'puede ocuparse.')
                self.intersects[r] = True
        # print('All intersections generated.')
        return True

    def create_intersects_nice(self, grid):
        for i in range(len(grid)):
            self.intersects.append(False)

        self.intersects[3] = True
        self.intersects[11] = True

        self.intersects[12] = True
        self.intersects[22] = True

        self.intersects[26] = True
        self.intersects[33] = True
        self.intersects[37] = True

        self.intersects[41] = True  # Fibonacci

        self.intersects[52] = True
        self.intersects[60] = True
        self.intersects[55] = True  # Hilbert

    def count_intersects(self):
        """
        Función que toma el (grid) total, evalúa cada punto y de ser True lo cuenta con el fín de retornar si es posible
        o no con la cantidad de espacios disponibles que debería generar luego para los puntos (dots).
        """
        length = len(self.menu.grafo.get_lista_vertices())
        c = 0
        for item in self.intersects:
            if item:  # Básicamente, al valer (True) adiciona el contador.
                c += 1
        if c == length:
            return True
        return False

    def load_images(self):
        """
        CLASE POR MEJORAR: No solo ha de cargar el patojito en posición casita, ha de cargar los diferentes sprites
        de los objetos cuando sea requerido.
        """
        wp = pygame.image.load(os.path.abspath(
            'V:/Unidades compartidas/Estructura de datos/Proyecto/Proyecto 02/V1.9 - ALT/assets/logo.png'
        ))
        l1 = pygame.image.load(os.path.abspath(
            'V:/Unidades compartidas/Estructura de datos/Proyecto/Proyecto 02/V1.8/assets/library_00.png'
        ))
        l2 = pygame.image.load(os.path.abspath(
            'V:/Unidades compartidas/Estructura de datos/Proyecto/Proyecto 02/V1.8/assets/library_01.png'
        ))
        r1 = pygame.image.load(os.path.abspath(
            'V:/Unidades compartidas/Estructura de datos/Proyecto/Proyecto 02/V1.8/assets/highway_00.png'
        ))
        r2 = pygame.image.load(os.path.abspath(
            'V:/Unidades compartidas/Estructura de datos/Proyecto/Proyecto 02/V1.8/assets/highway_01.png'
        ))

        wp_w, wp_h = (self.size[0] / 2), (self.size[1] / 2)
        img0_w, img0_h = (self.size[0] / 8), (self.size[1] / 6)
        img1_w, img1_h = (self.size[0] / 5), (self.size[1] / 3)
        # Dimensionamiento inicial | Transformar imágenes (mal escaladas).
        wp = pygame.transform.scale(wp, (wp_w, wp_h))
        l1 = pygame.transform.scale(l1, (img0_w, img0_h))
        l2 = pygame.transform.scale(l2, (img1_w, img1_h))
        r1 = pygame.transform.scale(r1, (img0_w, img0_h))
        r2 = pygame.transform.scale(r2, (img1_w, img1_h))

        return [wp, [l1, l2], [r1, r2]]
