#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 本文件只允许依赖math库
import math


def draw_line(p_list, algorithm):
    """绘制线段

    :param p_list: (list of list of int: [[x0, y0], [x1, y1]]) 线段的起点和终点坐标
    :param algorithm: (string) 绘制使用的算法，包括'DDA'和'Bresenham'，此处的'Naive'仅作为示例，测试时不会出现
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 绘制结果的像素点坐标列表
    """
    x0, y0 = p_list[0]
    x1, y1 = p_list[1]
    result = []
    if algorithm == 'Naive':
        if x0 == x1:
            for y in range(y0, y1 + 1):
                result.append((x0, y))
        else:
            if x0 > x1:
                x0, y0, x1, y1 = x1, y1, x0, y0
            k = (y1 - y0) / (x1 - x0)
            for x in range(x0, x1 + 1):
                result.append((x, int(y0 + k * (x - x0))))
    elif algorithm == 'DDA':
        if x0 == x1:
            for y in range(y0, y1 + 1):
                result.append((x0, y))
        else:
            steps = 0
            if abs(x1 - x0) >= abs(y1 - y0):
                steps = abs(x1 - x0)
            else:
                steps = abs(y1 - y0)

            dx = (x1 - x0)/steps
            dy = (y1 - y0)/steps
            x = x0 + 0.5
            y = y0 + 0.5

            for i in range(0, steps):
                result.append((int(x), int(y)))
                x += dx
                y += dy
            
    elif algorithm == 'Bresenham':
        if x0 == x1:
            for y in range(y0, y1 + 1):
                result.append((x0, y))
        else:
            dx = abs(x1 - x0)
            dy = abs(y1 - y0)
            sx = 1 if x0<x1 else -1
            sy = 1 if y0<y1 else -1
            
            err0 = dx if dx>dy else -dy 
            err = err0 / 2
            e2 = 0

            while True:
                result.append((x0, y0))
                if (x0==x1 and y0==y1):
                    break
                e2 = err
                if e2 > -dx:
                    err -= dy
                    x0 += sx
                if e2 < dy:
                    err += dx
                    y0 += sy
    return result


def draw_polygon(p_list, algorithm):
    """绘制多边形

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 多边形的顶点坐标列表
    :param algorithm: (string) 绘制使用的算法，包括'DDA'和'Bresenham'
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 绘制结果的像素点坐标列表
    """
    result = []
    for i in range(len(p_list)):
        line = draw_line([p_list[i - 1], p_list[i]], algorithm)
        result += line
    return result


def draw_ellipse(p_list):
    """绘制椭圆（采用中点圆生成算法）

    :param p_list: (list of list of int: [[x0, y0], [x1, y1]]) 椭圆的矩形包围框左上角和右下角顶点坐标
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 绘制结果的像素点坐标列表
    """
    x0, y0 = p_list[0]
    x1, y1 = p_list[1]
    result = []
    mx=int((x0+x1)/2)
    my=int((y0+y1)/2)
    a=int((abs(x1-x0))/2)
    b=int((abs(y1-y0))/2)
    p=float(b**2+a**2*(0.25-b))
    x=0
    y=b
    result.append((mx+x,my+y))
    result.append((mx-x,my+y))
    result.append((mx+x,my-y))
    result.append((mx-x,my-y))
    while(b**2*x < a**2*y):
        if(p<0):
            p+=float(b**2*(2*x+3))
        else:
            p+=float(b**2*(2*x+3)-a**2*(2*y-2))
            y-=1
        x+=1
        result.append((mx+x,my+y))
        result.append((mx-x,my+y))
        result.append((mx+x,my-y))
        result.append((mx-x,my-y))
    p=float((b*(x+0.5))**2+(a*(y-1))**2-(a*b)**2)
    while(y>0):
        if(p<0):
            p+=float(b**2*(2*x+2)+a**2*(-2*y+3))
            x+=1
        else:
            p+=float(a**2*(-2*y+3))
        y-=1
        result.append((mx+x,my+y))
        result.append((mx-x,my+y))
        result.append((mx+x,my-y))
        result.append((mx-x,my-y))
    return result



def draw_curve(p_list, algorithm):
    """绘制曲线

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 曲线的控制点坐标列表
    :param algorithm: (string) 绘制使用的算法，包括'Bezier'和'B-spline'（三次均匀B样条曲线，曲线不必经过首末控制点）
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 绘制结果的像素点坐标列表
    """
    


def translate(p_list, dx, dy):
    """平移变换

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param dx: (int) 水平方向平移量
    :param dy: (int) 垂直方向平移量
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    result = []
    for x,y in p_list:
        result.append((x + dx, y + dy))
    
    return result



def rotate(p_list, x, y, r):
    """旋转变换（除椭圆外）

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param x: (int) 旋转中心x坐标
    :param y: (int) 旋转中心y坐标
    :param r: (int) 顺时针旋转角度（°）
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    angel=float(r*math.pi/180)
    cos=math.cos(angel)
    sin=-math.sin(angel)
    result = []
    for x0, y0 in p_list:
        x1=int(float(x)+float((x0-x)*cos)-float((y0-y)*sin)+0.5)
        y1=int(float(y)+float((x0-x)*sin)+float((y0-y)*cos)+0.5)
        result.append((x1,y1))
    return result


def scale(p_list, x, y, s):
    """缩放变换

    :param p_list: (list of list of int: [[x0, y0], [x1, y1], [x2, y2], ...]) 图元参数
    :param x: (int) 缩放中心x坐标
    :param y: (int) 缩放中心y坐标
    :param s: (float) 缩放倍数
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1], [x_2, y_2], ...]) 变换后的图元参数
    """
    result = []
    for x0, y0 in p_list:
        x1=int(float(x0*s)+float(x*(1-s))+0.5)
        y1=int(float(y0*s)+float(y*(1-s))+0.5)
        result.append((x1,y1))
    return result


def clip(p_list, x_min, y_min, x_max, y_max, algorithm):
    """线段裁剪

    :param p_list: (list of list of int: [[x0, y0], [x1, y1]]) 线段的起点和终点坐标
    :param x_min: 裁剪窗口左上角x坐标
    :param y_min: 裁剪窗口左上角y坐标
    :param x_max: 裁剪窗口右下角x坐标
    :param y_max: 裁剪窗口右下角y坐标
    :param algorithm: (string) 使用的裁剪算法，包括'Cohen-Sutherland'和'Liang-Barsky'
    :return: (list of list of int: [[x_0, y_0], [x_1, y_1]]) 裁剪后线段的起点和终点坐标
    """
    
