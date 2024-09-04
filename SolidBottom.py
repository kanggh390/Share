from OCC.Core.gp import gp_Pnt, gp_Dir, gp_Ax1, gp_Trsf, gp_Vec, gp_Pln, gp_Circ, gp_Ax2
from OCC.Core.Geom import Geom_Line
from OCC.Core.BRepBuilderAPI import BRepBuilderAPI_MakeEdge, BRepBuilderAPI_MakeWire, BRepBuilderAPI_MakeFace, BRepBuilderAPI_Transform
from OCC.Core.BRepPrimAPI import BRepPrimAPI_MakePrism
from OCC.Core.BRepOffsetAPI import BRepOffsetAPI_MakePipe
from OCC.Core.BRepFilletAPI import BRepFilletAPI_MakeFillet
from OCC.Extend.TopologyUtils import TopologyExplorer
from OCC.Core.BRepAlgoAPI import BRepAlgoAPI_Cut

def create_face(points):
    # 점 정의
    for i in range(len(points)):
        points[i] = gp_Pnt(*points[i])

    # 엣지 정의
    edges = []
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        edges.append(edge)
    edges.append(BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge())

    # 와이어 정의
    wire_maker = BRepBuilderAPI_MakeWire()
    for edge in edges:
        wire_maker.Add(edge)
    wire = wire_maker.Wire()



    # 평면 생성
    face_maker = BRepBuilderAPI_MakeFace(wire)
    face = face_maker.Face()

    return face

def create_face1(points):
    # 점 정의
    for i in range(len(points)):
        points[i] = gp_Pnt(*points[i])

    # 엣지 정의
    edges = []
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        edges.append(edge)
    edges.append(BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge())

    # 와이어 정의
    wire_maker = BRepBuilderAPI_MakeWire()
    for edge in edges:
        wire_maker.Add(edge)
    wire = wire_maker.Wire()
    face_maker = BRepBuilderAPI_MakeFace(wire)
    face = face_maker.Face()

    return face

def create_face111(points):
    # 점 정의
    for i in range(len(points)):
        points[i] = gp_Pnt(*points[i])

    # 엣지 정의
    edges = []
    for i in range(len(points) - 1):
        edge = BRepBuilderAPI_MakeEdge(points[i], points[i + 1]).Edge()
        edges.append(edge)
    edges.append(BRepBuilderAPI_MakeEdge(points[-1], points[0]).Edge())

    # 와이어 정의
    wire_maker = BRepBuilderAPI_MakeWire()
    for edge in edges:
        wire_maker.Add(edge)
    wire = wire_maker.Wire()
    face_maker = BRepBuilderAPI_MakeFace(wire)
    face = face_maker.Face()

    return face

def create_straghit_solid(face, extrusion_distance):
    # 평면을 기준으로 꺼내기
    solid = BRepPrimAPI_MakePrism(face, gp_Vec(0, 0, extrusion_distance)).Shape()

    return solid

def create_straghit_solid1(face, extrusion_distance):
    # 평면을 기준으로 꺼내기
    solid = BRepPrimAPI_MakePrism(face, gp_Vec(0, -extrusion_distance, 0)).Shape()

    return solid

def create_elbow_solid(face):
    # 돌출될 경로 생성
    center = gp_Pnt(0, 0, 0)
    axis = gp_Ax2(center, gp_Dir(0, 1, 0))
    radius = 500
    angle = 90 * (3.141592653589793 / 180)  # 각도 90도 (라디안으로 변환)
    arc = gp_Circ(axis, radius)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, 0, angle).Edge()



    # 경로를 와이어로 변환
    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()

    # 평면을 기준으로 꺼내기
    solid = BRepOffsetAPI_MakePipe(path_wire, face).Shape()

    return solid

def create_cylinder11(point, radius, y):
    center = gp_Pnt(point[0], point[1], point[2])
    axis = gp_Ax2(center, gp_Dir(0, 1, 0))
    arc = gp_Circ(axis, radius)
    angle = 360 * (3.141592653589793 / 180)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, angle, 0).Edge()

    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()
    face_maker = BRepBuilderAPI_MakeFace(path_wire)
    face = face_maker.Face()
    solid_cylinder = create_straghit_solid1(face, y)

    return solid_cylinder



def create_cylinder(point):
    center = gp_Pnt(point[0], point[1], 0.0096)
    axis = gp_Ax2(center, gp_Dir(0, 0, 1))
    arc = gp_Circ(axis, 0.0024)
    angle = 360 * (3.141592653589793 / 180)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, 0, angle).Edge()

    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()
    face_maker = BRepBuilderAPI_MakeFace(path_wire)
    face = face_maker.Face()
    solid_cylinder = create_straghit_solid(face, 0.0019)

    return solid_cylinder


def create_cylinder1(point):
    center = gp_Pnt(point[0], point[1], 0.0192)
    axis = gp_Ax2(center, gp_Dir(0, 0, 1))
    arc = gp_Circ(axis, 0.0024)
    angle = 360 * (3.141592653589793 / 180)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, 0, angle).Edge()

    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()
    face_maker = BRepBuilderAPI_MakeFace(path_wire)
    face = face_maker.Face()
    solid_cylinder = create_straghit_solid(face, 0.0019)

    return solid_cylinder
def create_cylinder2(point):
    center = gp_Pnt(point[0], point[1], 0.0288)
    axis = gp_Ax2(center, gp_Dir(0, 0, 1))
    arc = gp_Circ(axis, 0.0024)
    angle = 360 * (3.141592653589793 / 180)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, 0, angle).Edge()

    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()
    face_maker = BRepBuilderAPI_MakeFace(path_wire)
    face = face_maker.Face()
    solid_cylinder = create_straghit_solid(face, 0.0019)

    return solid_cylinder

def create_cylinder3(point):
    center = gp_Pnt(point[0], point[1], 15)
    axis = gp_Ax2(center, gp_Dir(0, 0, 1))
    arc = gp_Circ(axis, 0.0024)
    angle = -270 * (3.141592653589793 / 180)
    arc_edge = BRepBuilderAPI_MakeEdge(arc, 0, angle).Edge()

    path_wire = BRepBuilderAPI_MakeWire(arc_edge).Wire()
    face_maker = BRepBuilderAPI_MakeFace(path_wire)
    face = face_maker.Face()
    solid_cylinder = create_straghit_solid(face, 100)

    return solid_cylinder


if __name__ == "__main__":
    # 평면 생성
    face = create_face([[0, 0, 0], [10, 0, 0], [10, 10, 0], [0, 10, 0]])

    # 평면을 기준으로 꺼내기
    solid = create_straghit_solid(face, 10)

