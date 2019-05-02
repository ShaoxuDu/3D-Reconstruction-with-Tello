# Tello-Python

## Introduction

这是一组基于python的示例代码，与Tello无人机交互.

## Project Description

这个项目包含两个基于Tello SDK和python 2.7 的示例程序，包括Single_Tello_Test和Tello_Video(With_Pose_Recognition). 一个包含一些官方文档的文件夹，一个包含一些程序依赖的文件夹，还有一个名为tello_state.py的文件.

- **Single_Tello_Test**

在Single_Tello_Test中，可以通过编写txt脚本来设计一系列命令组合，让Tello执行设计的一系列操作。这个程序也可以用作Tello的命令集测试工具。

- **Tello_Video(With_Pose_Recognition)**

 在Tello_Video(With_Pose_Recognition),可以从Tello接收视频流数据,解码通过h264视频解码库,并将其在一个基于Tkinter和PIL的GUI接口上显示。也可通过提前规划路线，操作Tello按指定轨迹运动并在指定位置拍摄图片。此外，它还支持一个可以操作Tello的控制面板。此示例代码提供了接收、处理和获取正确视频数据的示例。包中还提供了h264解码库的源代码，供您参考。


Tello_Video_With_Pose_Recognition是Tello_Video修改后的应用程序版本。它使用了视频数据解码,每次提取单帧图像构成识别操作,并结合特定的姿势和飞机控制命令来实现Tello的姿态控制。该代码主要用于将tello解码后的视频数据用于图像处理的应用实例。

- **Tello_state.py**

 读取tello的各种状态数据，可以作为调试和查看tello状态的工具。

- **Document**

 包括两个官方文档，一个是基本指令的调用方法，另一个是关于h264解码的一系列视频流传输问题的FAQ。

- **tello_video_dll(ForWin64)**

 包括实现h264解码的一些dll依赖，需要将其放置在对应python版本的site-packages中

## Environmental configuration
 
 实例程序在WIN64，python 2.7 的环境中运行，需要安装多个库如pillow，numpy等(opencv包可能需要通过直接保存对应的whl文件到site-packages中)




