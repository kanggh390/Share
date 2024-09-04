import numpy as np
import math
def offset_line_inside(start, end, offset):
    # 선분의 방향 벡터 계산
    direction = np.array(end) - np.array(start)
    direction[0] /= np.linalg.norm(direction)
    direction[1] /= np.linalg.norm(direction)
    #print(direction[0], direction[1])
    # 선분의 정규 법선 벡터 계산 (왼쪽으로 이동)
    normal = np.array([direction[1], -direction[0]])
    #print(normal)
    # 오프셋 된 점들 계산
    offset_start = np.array(start) + offset * normal
    offset_end = np.array(end) + offset * normal

    return offset_start, offset_end

def offset_connected_lines_inside(points, offset):
    offset_lines = []

    for i in range(len(points) - 1):
        start = points[i]
        end = points[i + 1]

        offset_start, offset_end = offset_line_inside(start, end, offset)

        # 오프셋 값만큼 양쪽 끝을 자르기
        offset_start_cut = np.array(start) + offset * (np.array(offset_start) - np.array(start)) / np.linalg.norm(np.array(offset_start) - np.array(start))
        offset_end_cut = np.array(end) + offset * (np.array(offset_end) - np.array(end)) / np.linalg.norm(np.array(offset_end) - np.array(end))

        offset_lines.append((offset_start_cut, offset_end_cut))

    return offset_lines

def find_intersection(line1, line2):
    x1, y1 = line1[0]
    x2, y2 = line1[1]
    x3, y3 = line2[0]
    x4, y4 = line2[1]

    # 두 선이 수직인 경우
    if x2 - x1 == 0 and x4 - x3 == 0:
        if x1 != x3:
            return None
        # 두 선이 수직이고 겹치는 경우
        y_intersection_min = max(min(y1, y2), min(y3, y4))
        y_intersection_max = min(max(y1, y2), max(y3, y4))
        return (x1, y_intersection_min) if y_intersection_min <= y_intersection_max else None

    # 두 선이 y축과 평행한 경우
    if x2 - x1 == 0:
        x_intersection = x1
        m2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('nan')
        b2 = y3 - m2 * x3 if not math.isnan(m2) else x3
        y_intersection = m2 * x_intersection + b2
        return x_intersection, y_intersection

    if x4 - x3 == 0:
        x_intersection = x3
        m1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('nan')
        b1 = y1 - m1 * x1 if not math.isnan(m1) else x1
        y_intersection = m1 * x_intersection + b1
        return x_intersection, y_intersection

    # 두 선의 기울기 계산
    m1 = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('nan')
    m2 = (y4 - y3) / (x4 - x3) if x4 - x3 != 0 else float('nan')

    # 두 선이 평행한 경우
    if m1 == m2:
        return None

    # 두 선의 y-절편 계산
    b1 = y1 - m1 * x1 if not math.isnan(m1) else x1
    b2 = y3 - m2 * x3 if not math.isnan(m2) else x3

    # 교차점의 x좌표 계산
    if math.isnan(m1):
        x_intersection = x1
    elif math.isnan(m2):
        x_intersection = x3
    else:
        x_intersection = (b2 - b1) / (m1 - m2)

    # 교차점의 y좌표 계산
    y_intersection = m1 * x_intersection + b1

    return x_intersection, y_intersection

# 오프셋 값 설정
offset_value = 1.0

def make_sketchpoint(line_points, offset_value):

    # 선분 안쪽으로 오프셋 계산
    offset_lines = offset_connected_lines_inside(line_points, offset_value)
    print(offset_lines)
    line_list = []

    # 오프셋된 선들을 리스트에 추가하고 교차점을 찾아줌
    for i in offset_lines:
        line_list.append([i[0].tolist(),i[1].tolist()])

    for i in range(len(line_list)-1):
        intersection = find_intersection(line_list[i], line_list[i + 1])
        line_list[i][1] = [intersection[0], intersection[1]]
        line_list[i+1][0] = [intersection[0], intersection[1]]
    print(line_list)
    # 원래의 선들도 리스트에 추가시켜줌
    for i in range(len(line_points)-1):
        line_list.append([line_points[i+1],line_points[i]])

    # 선의 시작과 끝에 연결되지않은부분을 연결해줌
    line_list.append([offset_lines[-1][1].tolist(), line_points[-1]])
    line_list.append([line_points[0],offset_lines[0][0].tolist()])

    # print(line_list)
    sketch_point = []
    for i in range(len(line_list)):
        if i == 0:
            sketch_point.append(line_list[i])
            line_list.remove(line_list[i])
        else:
            for line in line_list:
                if sketch_point[-1][1] == line[0] :
                    sketch_point.append(line)
                    line_list.remove(line)
                    break
                elif sketch_point[-1][1] == line[1] :
                    sketch_point.append([line[1], line[0]])
                    line_list.remove(line)
                    break
                else:
                    pass
    last_sketch_point = []
    for i in range(len(sketch_point)):
        last_sketch_point.append(sketch_point[i][0])

    return last_sketch_point