import tello
from tello_control_ui import TelloUI
import time
import math


def send_command(drone, commands):
    for c in commands:
        if c.find('delay') != -1:
            sec = float(c.partition('delay')[2])
            print 'delay %s' % sec
            time.sleep(sec)
            pass
        else:
            drone.send_command(c)

def main():

    drone = tello.Tello()
    # 
    ##### Manual control through UI interface #####
    # vplayer = TelloUI(drone, "./img/")
    # vplayer.root.mainloop()

    ##### Automatic Control of Advance Planning Route #####
    # move_distance > 20 cm, 360 % rotate_degrees == 0
    radius = 100 
    rotate_degrees = 18
    rotate_times = 360 // rotate_degrees
    move_distance = int(2 * radius * math.sin(rotate_degrees * math.pi / 360))

    rotate_command = 'ccw ' + str(rotate_degrees // 2)
    start_command = ['command', 'takeoff', 'delay 10', 'forward ' + str(radius), 'cw 180']
    loop_command = [rotate_command, 'right ' + str(move_distance), rotate_command]
    end_command = ['forward ' + str(radius), 'cw 180', 'land']

    drone.set_speed(100)

    # Takeoff from the center of a circle and Get to the edge
    send_command(drone, start_command)
    
    # Circumferential motion around the center of a circle
    for i in range(rotate_times):
        send_command(drone, loop_command)
        # save image
        drone.save_current_frame()
    # Come back to the center and Land
    send_command(drone, end_command)


if __name__ == "__main__":
    main()
