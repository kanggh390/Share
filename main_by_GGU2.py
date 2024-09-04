from os import environ

from OCC.Core.AIS import AIS_ColoredShape
import OCC.Core.V3d
from PyQt5.QtWidgets import *
from PyQt5 import uic
from OCC.Display.backend import load_backend
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Fuse
load_backend('pyqt5')
import OCC.Display.qtDisplay as qtDisplay
import sys
from SolidBottom import *
from OCC.Core.Quantity import *
from OCC.Core.V3d import V3d_DirectionalLight, V3d_View, V3d_Trihedron, V3d_AmbientLight
from OCC.Core.V3d import V3d_SpotLight
from OCC.Core.Graphic3d import *
from OCC.Core.Aspect import Aspect_IS_SOLID, Aspect_GFM_VER, Aspect_GFM_VER
from OCC.Core.StlAPI import StlAPI_Writer
from OCC.Core.Graphic3d import *
from OCC.Core.Quantity import Quantity_Color, Quantity_NOC_WHITE, Quantity_NOC_BROWN
from OCC.Core.AIS import AIS_Shape
from OCC.Core.Aspect import Aspect_IS_SOLID
from OCC.Core.gp import gp_Pnt

from OCC.Core.gp import gp_Ax2, gp_Dir
from OCC.Core.V3d import (
    V3d_XposYposZpos,
    V3d_XposYnegZpos,
    V3d_XposYposZneg,
    V3d_XnegYposZpos,
    V3d_XposYnegZneg,
    V3d_XnegYposZneg,
    V3d_XnegYnegZpos,
    V3d_XnegYnegZneg
)
import trimesh
name = "none"
camera_factors = [V3d_XposYposZpos,
                  V3d_XposYnegZpos,
                  V3d_XposYposZneg,
                  V3d_XnegYposZpos,
                  V3d_XposYnegZneg,
                  V3d_XnegYposZneg,
                  V3d_XnegYnegZpos,
                  V3d_XnegYnegZneg]

mainwindow_ui = uic.loadUiType('GUI/mainwindow.ui')[0]


class mainwindow(QMainWindow, mainwindow_ui):
    def __init__(self):
        super(mainwindow, self).__init__()
        mainwindow_ui = "GUI/mainwindow.ui"
        uic.loadUi(mainwindow_ui, self)

        # 여기서 OCC 뷰어 초기화
        self.canvas = qtDisplay.qtViewer3d(self)
        self.canvas.InitDriver()
        self.display = self.canvas._display
        # self.display.SetSize(224, 224)
        self.verticalLayout.addWidget(self.canvas)
        self.setLayout(self.verticalLayout_3)

        self.initUI()

    def initUI(self):
        self.makerButton.clicked.connect(self.Lego_list)

    def Lego_list(self):
        # self.make_Lego1()
        # self.make_Lego2()
        self.make_Lego3()
        self.make_Lego4()

    def make_Lego4(self):
        name = "Lego4"
        Tlqkf_15 = []
        garo = 4
        sero = 2
        self.make_under_white_block(garo, sero)
        Tlqkf_15.append(self.make_Lego_RED_block_Left(2,4,0))
        Tlqkf_15.append(self.make_Lego_RED_block_right(4,2,2, 0))
        Tlqkf_15.append(self.make_Lego_RED_block_Right_move_y(0,2,2,0,2))
        Tlqkf_15.append(self.make_Lego_RED_block_Left(3,2,0.0096))
        Tlqkf_15.append(self.make_Lego_RED_block_right(4,2,1,0.0096))
        Tlqkf_15.append(self.make_Lego_RED_block_Right_move_y(2,2,3, 0.0096, 2))
        Tlqkf_15.append(self.make_Lego_RED_block_Right_move_y(-1, 2, 1, 0.0096, 2))
        Tlqkf_15.append(self.make_Lego_RED_Cylinder_block_2nd(4,2,0))
        Tlqkf_15.append(self.make_Lego_RED_Cylinder_block_2nd_move_y(4, 2, -2, 2))
        Tlqkf15 = BRepAlgoAPI_Fuse(Tlqkf_15[0], Tlqkf_15[1])
        for i in range(len(Tlqkf_15) - 2):
            Tlqkf15 = BRepAlgoAPI_Fuse(Tlqkf15.Shape(), Tlqkf_15[i + 2])
        Tlqkf15_shape = Tlqkf15.Shape()
        self.export_to_stl(Tlqkf15_shape, "Lego4.stl")
        self.exchange_stl_to_obj("Lego4.stl", "Lego4.obj")
        # self.display.EraseAll()
        self.image_save_Tlqkf(name)



    def make_Lego3(self):
        name = "Lego3"
        TLqkf_13 = []
        garo = 4
        sero = 2
        self.make_under_white_block(garo, sero)
        TLqkf_13.append(self.make_Lego_RED_block_Left(garo, sero, 0))
        TLqkf_13.append(self.make_Lego_RED_Cylinder_block_1st(2, 2, 2))
        TLqkf_13.append(self.make_Lego_RED_block_Left(2,1, 0.0096))
        TLqkf_13.append(self.make_Lego_RED_block_Left_move_y(2, 1, 0.0096, 1))
        TLqkf_13.append(self.make_Lego_RED_Cylinder_block_2nd(2,2, 0))
        Tlqkf13 = BRepAlgoAPI_Fuse(TLqkf_13[0], TLqkf_13[1])
        for i in range(len(TLqkf_13) - 2):
            Tlqkf13 = BRepAlgoAPI_Fuse(Tlqkf13.Shape(), TLqkf_13[i + 2])
        Tlqkf13_shape = Tlqkf13.Shape()
        self.export_to_stl(Tlqkf13_shape, "Lego3.stl")
        self.exchange_stl_to_obj("Lego3.stl", "Lego3.obj")
        # self.display.EraseAll()



        self.image_save_Tlqkf(name)


    def make_Lego2(self):
        name = "Lego2"
        Tlqkf_14 = []
        garo = 6
        sero = 2
        self.make_under_white_block(garo, sero)
        Tlqkf_14.append(self.make_Lego_RED_block_Left(3, sero, 0))
        Tlqkf_14.append(self.make_Lego_RED_block_right(garo, sero, 1, 0))
        Tlqkf_14.append(self.make_Lego_RED_block_right(5, 2, 2, 0))
        Tlqkf_14.append(self.make_Lego_RED_block_Left(2,2,0.0096))
        Tlqkf_14.append(self.make_Lego_RED_block_right(4, 2, 2,0.0096))
        Tlqkf_14.append(self.make_Lego_RED_block_right(garo, sero, 2, 0.0096))
        Tlqkf_14.append(self.make_Lego_RED_Cylinder_block_2nd(2, 2, 0))
        Tlqkf_14.append(self.make_Lego_RED_Cylinder_block_2nd(2,2,2))
        Tlqkf_14.append(self.make_Lego_RED_Cylinder_block_2nd(2,2,4))
        Tlqkf14 = BRepAlgoAPI_Fuse(Tlqkf_14[0], Tlqkf_14[1])
        for i in range(len(Tlqkf_14) - 2):
            Tlqkf14 = BRepAlgoAPI_Fuse(Tlqkf14.Shape(), Tlqkf_14[i + 2])
        Tlqkf14_shape = Tlqkf14.Shape()
        self.export_to_stl(Tlqkf14_shape, "Lego2.stl")
        self.exchange_stl_to_obj("Lego2.stl", "Lego2.obj")
        # self.display.EraseAll()

        self.image_save_Tlqkf(name)


    def make_Lego1(self):
        name = "Lego1"
        garo = 4
        sero = 2
        Tlqkf_12 = []

        self.make_under_white_block(garo, sero)
        Tlqkf_12.append(self.make_Lego_RED_block_Left(garo, sero, 0))
        Tlqkf_12.append(self.make_Lego_RED_block_Left(1, sero, 0.0096))
        Tlqkf_12.append(self.make_Lego_RED_block_right(garo, sero, 1, 0.0096))
        Tlqkf_12.append(self.make_Lego_RED_block_Left(1, 2, 0.0192))
        Tlqkf_12.append(self.make_Lego_RED_block_right(garo, sero, 1, 0.0192))
        Tlqkf_12.append(self.make_Lego_RED_Cylinder_block_1st(2, 2, 1))
        Tlqkf_12.append(self.make_Lego_RED_Cylinder_block_3rd(1, 2, 0))
        Tlqkf_12.append(self.make_Lego_RED_Cylinder_block_3rd(1,2, 3))
        # Tlqkf12 = BRepAlgoAPI_Fuse(Tlqkf_12[0], Tlqkf_12[1])
        # for i in range(len(Tlqkf_12) - 2):
        #     Tlqkf12 = BRepAlgoAPI_Fuse(Tlqkf12.Shape(), Tlqkf_12[i + 2])
        # Tlqkf12_shape = Tlqkf12.Shape()
        # self.export_to_stl(Tlqkf12_shape, "Lego1.stl")
        # self.exchange_stl_to_obj("Lego1.stl", "Lego1.obj")
        #
        # self.display.EraseAll()
        #
        self.image_save_Tlqkf(name)


    def make_Lego_RED_Cylinder_block_1st(self, garo, sero, space):
        cylinder_Block = []
        for i in range(garo):
            for j in range(sero):
                solid_cylinder = create_cylinder([space*0.0079+0.00395+i*0.0079, 0.00395+j*0.0079])
                cylinder_Block.append(solid_cylinder)
                self.viewer(solid_cylinder, Quantity_NOC_RED, 0.0)
        Cylinder_Block = BRepAlgoAPI_Fuse(cylinder_Block[0], cylinder_Block[1])
        for i in range(len(cylinder_Block) - 2):
            Cylinder_Block = BRepAlgoAPI_Fuse(Cylinder_Block.Shape(), cylinder_Block[i + 2])
        Cylinder_Block = Cylinder_Block.Shape()

        return Cylinder_Block

    def make_Lego_RED_Cylinder_block_2nd_move_y(self, garo, sero, space, move):
        cylinder_Block=[]
        for i in range(garo):
            for j in range(sero):
                solid_cylinder = create_cylinder1([space*0.0079+0.00395+i*0.0079, 0.00395+0.0079*j+move*0.0079])
                cylinder_Block.append(solid_cylinder)
                self.viewer(solid_cylinder, Quantity_NOC_RED, 0.0)
        Cylinder_Block = BRepAlgoAPI_Fuse(cylinder_Block[0], cylinder_Block[1])
        for i in range(len(cylinder_Block) - 2):
            Cylinder_Block = BRepAlgoAPI_Fuse(Cylinder_Block.Shape(), cylinder_Block[i + 2])
        Cylinder_Block = Cylinder_Block.Shape()

        return Cylinder_Block

    def make_Lego_RED_Cylinder_block_2nd(self, garo, sero, space):
        cylinder_Block = []
        for i in range(garo):
            for j in range(sero):
                solid_cylinder = create_cylinder1([space*0.0079+0.00395+0.0079*i, 0.00395+0.0079*j])
                cylinder_Block.append(solid_cylinder)
                self.viewer(solid_cylinder, Quantity_NOC_RED, 0.0)
        Cylinder_Block = BRepAlgoAPI_Fuse(cylinder_Block[0], cylinder_Block[1])
        for i in range(len(cylinder_Block) - 2):
            Cylinder_Block = BRepAlgoAPI_Fuse(Cylinder_Block.Shape(), cylinder_Block[i + 2])
        Cylinder_Block = Cylinder_Block.Shape()

        return Cylinder_Block

    def make_Lego_RED_Cylinder_block_3rd(self, garo, sero, space):
        cylinder_Block = []
        for i in range(garo):
            for j in range(sero):
                solid_cylinder = create_cylinder2([space*0.0079+0.00395+i*0.0079, 0.00395+j*0.0079])
                cylinder_Block.append(solid_cylinder)
                self.viewer(solid_cylinder, Quantity_NOC_RED, 0.0)
        Cylinder_Block = BRepAlgoAPI_Fuse(cylinder_Block[0], cylinder_Block[1])
        for i in range(len(cylinder_Block) - 2):
            Cylinder_Block = BRepAlgoAPI_Fuse(Cylinder_Block.Shape(), cylinder_Block[i + 2])
        Cylinder_Block = Cylinder_Block.Shape()

        return Cylinder_Block


    def make_Lego_RED_block_right(self, garo, sero, garo1, hight):
        sketch_point = [[garo*0.0079, sero*0.0079], [garo*0.0079, 0], [garo*0.0079-garo1*0.0079, 0], [garo*0.0079-garo1*0.0079, sero*0.0079]]
        for point in sketch_point:
            point.append(hight)
        face = create_face(sketch_point)
        solid = create_straghit_solid(face, 0.0096)
        self.viewer(solid, Quantity_NOC_RED, 0.0)
        return solid

    def make_Lego_RED_block_Left(self, garo, sero, hight):
        sketch_point = [[0,0], [0, sero*0.0079], [garo*0.0079, sero*0.0079], [garo*0.0079, 0]]
        for point in sketch_point:
            point.append(hight)
        face = create_face(sketch_point)
        solid = create_straghit_solid(face, 0.0096)
        self.viewer(solid, Quantity_NOC_RED, 0.0)
        return solid

    def make_Lego_RED_block_Left_move_y(self, garo, sero, hight, move):
        sketch_point = [[0, move*0.0079], [0, move*0.0079 + sero*0.0079], [garo*0.0079, move*0.0079+sero*0.0079], [garo*0.0079, move*0.0079]]
        for point in sketch_point:
            point.append(hight)
        face = create_face(sketch_point)
        solid = create_straghit_solid(face, 0.0096)
        self.viewer(solid, Quantity_NOC_RED, 0.0)
        return solid

    def make_Lego_RED_block_Right_move_y(self, garo, sero, garo1, hight, move):
        sketch_point = [[garo * 0.0079, sero * 0.0079+move*0.0079], [garo * 0.0079, move*0.0079], [garo * 0.0079 - garo1 * 0.0079, move*0.0079],
                        [garo * 0.0079 - garo1 * 0.0079, sero * 0.0079+0.0079*move]]
        for point in sketch_point:
            point.append(hight)
        face = create_face(sketch_point)
        solid = create_straghit_solid(face, 0.0096)
        self.viewer(solid, Quantity_NOC_RED, 0.0)
        return solid

    def make_under_white_block(self, garo, sero):
        garo = garo * 10
        sero = sero * 10
        self.display.EraseAll()
        sketch_point = [[-0.0079*garo, -0.0079*sero], [-0.0079*garo, 0.0079*sero + 0.0079*sero/10], [0.0079*garo+0.0079*garo/10, 0.0079*sero + 0.0079*sero/10], [0.0079*garo+0.0079*garo/10, -0.0079*sero]]
        for point in sketch_point:
            point.append(-0.0019)
        face = create_face(sketch_point)
        solid = create_straghit_solid(face, 0.0019)
        self.viewer_whithe(solid, Quantity_NOC_WHITE, 0.0)




    def viewer(self, solid, Quantity_NOC_color, transparency_level):
        ais_shape = self.display.DisplayShape(solid, update=True)[0]
        back_ground = [0.5, 0.5, 0.5]
        color_rgb = [0.0, 0.0, 0.0]
        color_bg = Quantity_Color(*back_ground, Quantity_TOC_RGB)
        color = Quantity_Color(*color_rgb, Quantity_TOC_RGB)
        self.display.View.SetBackgroundColor(color_bg)

        aColoredShape = AIS_ColoredShape(solid)
        aColoredShape.SetCustomColor(solid, Quantity_Color(Quantity_NOC_color))

        self.display.Context.SetColor(ais_shape, color, False)
        self.display.Context.SetTransparency(ais_shape, transparency_level, False)
        self.display.GetContext().Display(aColoredShape, False)
        self.display.default_drawer.SetFaceBoundaryDraw(False)
        # self.display.SetRenderingParams(Method=Graphic3d_RM_RASTERIZATION,
        #                                 RaytracingDepth=3, IsShadowEnabled=True, IsTransparentShadowEnabled=True)
        # self.display.SetRaytracingMode(depth=3)
        self.display.DisplayColoredShape(solid, color="RED", update=False)
        # self.display.DisplayShape(solid, material=Graphic3d_NOM_TRANSPARENT, texture=None, color=Quantity_NOC_color,
        #                           transparency=None, update=True)
        self.display.View.SetLightOff()
        # self.setup_lighting()

        self.display.ZoomFactor(7.0)
        self.display.View.SetProj(V3d_XposYposZpos)

    def export_to_stl(self, shape, filename):
        writer = StlAPI_Writer()
        writer.Write(shape, filename)

    def exchange_stl_to_obj(self, export_file_name, output_file_name):
        mesh = trimesh.load(export_file_name)
        mesh.export(output_file_name)
    def viewer_whithe(self, solid, Quantity_NOC_color, transparency_level):
        self.display.EraseAll()
        ais_shape = self.display.DisplayShape(solid, update=True)[0]
        back_ground = [0.5, 0.5, 0.5]
        color_rgb = [0.0, 0.0, 0.0]
        color_bg = Quantity_Color(*back_ground, Quantity_TOC_RGB)
        color = Quantity_Color(*color_rgb, Quantity_TOC_RGB)
        self.display.View.SetBackgroundColor(color_bg)

        aColoredShape = AIS_ColoredShape(solid)
        aColoredShape.SetCustomColor(solid, Quantity_Color(Quantity_NOC_color))

        self.display.Context.SetColor(ais_shape, color, False)
        self.display.Context.SetTransparency(ais_shape, transparency_level, False)
        self.display.GetContext().Display(aColoredShape, False)
        self.display.default_drawer.SetFaceBoundaryDraw(False)
        # self.display.SetRenderingParams(Method=Graphic3d_RM_RASTERIZATION,
        #                                 RaytracingDepth=3, IsShadowEnabled=True, IsTransparentShadowEnabled=True)
        # self.display.SetRaytracingMode(depth=3)
        self.display.DisplayColoredShape(solid, color="WHITE", update=False)
        # self.display.DisplayShape(solid, material=Graphic3d_NOM_SHINY_PLASTIC, texture=None, color=Quantity_NOC_color,
        #                           transparency=None, update=True)
        self.display.View.SetLightOff()
        self.setup_lighting()

        self.display.FitAll()
    # def image_save_Tlqkf(self, name):
    #     p = 0
    #     for camera_factor in camera_factors:
    #         self.display.FitAll()
    #         self.display.ZoomFactor(7.0)
    #         self.display.View.SetProj(camera_factor)
    #         # camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/NEW_{name}_{p}.jpg"
    #         # self.display.View.Dump(camera_factor_path)
    #         p+=1
    def image_save_Tlqkf(self, name):
        p = 0

        for angle in range(0, 360, 1):
            ax2 = gp_Ax2()
            ax2.SetDirection(gp_Dir(1, 1, 0.5))  # X-axis 방향으로 설정
            # 1번 : gp_Dir(-1, 1, -1)
            ax1 = gp_Ax1(ax2.Location(), gp_Dir(0, 0, 1))
            ax2.Rotate(ax1, angle * (3.14159265 / 180))

            direction = ax2.Direction()
            x, y, z = direction.X(), direction.Y(), direction.Z()

            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(8.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)
            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(7.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

            p += 1
            self.display.FitAll()
            self.display.ZoomFactor(6.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

        for angle in range(0, 360, 1):
            ax2 = gp_Ax2()
            ax2.SetDirection(gp_Dir(1, 1, 0.5))  # X-axis 방향으로 설정
            # 1번 : gp_Dir(-1, 1, -1)
            ax1 = gp_Ax1(ax2.Location(), gp_Dir(0, 0, -0.7))
            ax2.Rotate(ax1, angle * (3.14159265 / 180))

            direction = ax2.Direction()
            x, y, z = direction.X(), direction.Y(), direction.Z()

            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(8.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)
            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(7.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

            p += 1
            self.display.FitAll()
            self.display.ZoomFactor(6.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

        for angle in range(0, 180, 1):
            ax2 = gp_Ax2()
            ax2.SetDirection(gp_Dir(-1, 0, 1))  # X-axis 방향으로 설정
            # 1번 : gp_Dir(-1, 1, -1)
            ax1 = gp_Ax1(ax2.Location(), gp_Dir(0, 1, 1))
            ax2.Rotate(ax1, angle * (3.14159265 / 180))

            direction = ax2.Direction()
            x, y, z = direction.X(), direction.Y(), direction.Z()

            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(8.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)
            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(7.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

            p += 1
            self.display.FitAll()
            self.display.ZoomFactor(6.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

        for angle in range(0, 180, 1):
            ax2 = gp_Ax2()
            ax2.SetDirection(gp_Dir(0, 1, 0))  # X-axis 방향으로 설정
            # 1번 : gp_Dir(-1, 1, -1)
            ax1 = gp_Ax1(ax2.Location(), gp_Dir(1, 0, 1))
            ax2.Rotate(ax1, angle * (3.14159265 / 180))

            direction = ax2.Direction()
            x, y, z = direction.X(), direction.Y(), direction.Z()

            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(8.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)
            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(7.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

            p += 1
            self.display.FitAll()
            self.display.ZoomFactor(6.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

        for angle in range(0, 180, 1):
            ax2 = gp_Ax2()
            ax2.SetDirection(gp_Dir(-1, 0, 0.5))  # X-axis 방향으로 설정
            # 1번 : gp_Dir(-1, 1, -1)
            ax1 = gp_Ax1(ax2.Location(), gp_Dir(0, 0.5, 0.5))
            ax2.Rotate(ax1, angle * (3.14159265 / 180))

            direction = ax2.Direction()
            x, y, z = direction.X(), direction.Y(), direction.Z()

            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(8.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)
            p += 1
            self.display.View.SetProj(x, y, z)
            self.display.FitAll()
            self.display.ZoomFactor(7.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

            p += 1
            self.display.FitAll()
            self.display.ZoomFactor(6.0)
            camera_factor_path = f"C:/OCC_py/pythonProject/get_image/{name}/{name}_{p}.jpg"
            self.display.View.Dump(camera_factor_path)

        self.display.View_Iso()
        self.display.FitAll()

    def setup_lighting(self):

        # 주변광 설정
        ambient_light_color = Quantity_Color(Quantity_NOC_WHITE)
        ambient_light = V3d_AmbientLight(ambient_light_color)
        self.display.Viewer.AddLight(ambient_light)
        self.display.Viewer.SetLightOn(ambient_light)

        # 물체를 비추는 조명 설정
        # 물체의 위치와 크기에 맞추어 조명 위치와 방향을 설정
        # 물체가 (0,0,0)에 있고 크기가 가로 5, 세로 5, 높이 10일 때

        # 위에서 비추는 방향광
        light_direction_top = gp_Dir(0, 0, -1)  # 위쪽에서 아래로 비추는 방향
        directional_light_top = V3d_DirectionalLight(light_direction_top)
        directional_light_top.SetColor(Quantity_Color(Quantity_NOC_WHITE))
        directional_light_top.SetIntensity(0.02)
        self.display.Viewer.AddLight(directional_light_top)
        self.display.Viewer.SetLightOn(directional_light_top)

        # 측면에서 비추는 방향광
        light_direction_side = gp_Dir(-1, -1, -1)  # 측면에서 비추는 방향
        directional_light_side = V3d_DirectionalLight(light_direction_side)
        directional_light_side.SetColor(Quantity_Color(Quantity_NOC_WHITE))
        directional_light_side.SetIntensity(0.02)
        self.display.Viewer.AddLight(directional_light_side)
        self.display.Viewer.SetLightOn(directional_light_side)

        # 측면에서 비추는 방향광
        light_direction_side_2 = gp_Dir(-1, -1, 0)  # 측면에서 비추는 방향
        directional_light_side_2 = V3d_DirectionalLight(light_direction_side_2)
        directional_light_side_2.SetColor(Quantity_Color(Quantity_NOC_WHITE))
        directional_light_side_2.SetIntensity(0.02)
        self.display.Viewer.AddLight(directional_light_side_2)
        self.display.Viewer.SetLightOn(directional_light_side_2)





def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"] = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"] = "1"
    environ["QT_SCALE_FACTOR"] = "1"


if __name__ == "__main__":
    suppress_qt_warnings()
    app = QApplication(sys.argv)
    myWindow = mainwindow()
    myWindow.show()
    app.exec_()