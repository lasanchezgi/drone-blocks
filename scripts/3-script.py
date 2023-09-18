from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = 'e7330db9-663b-424c-8774-ecd413c15bba'
    distance = 40
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        drone.takeoff()
        drone.fly_forward(20, 'in')
        drone.fly_backward(20, 'in')
        drone.fly_left(20, 'in')
        drone.fly_right(20, 'in')
        drone.fly_up(20, 'in')
        drone.fly_down(20, 'in')
        drone.fly_to_xyz(10, 20, 30, 'in')
        drone.fly_curve(25, 25, 0, 0, 50, 0, 'in')
        drone.flip_forward()
        drone.flip_backward()
        drone.flip_left()
        drone.flip_right()
        drone.land()