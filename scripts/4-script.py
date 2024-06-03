# Laura Alejandra Sánchez Giraldo

from DroneBlocksTelloSimulator.DroneBlocksSimulatorContextManager import DroneBlocksSimulatorContextManager

if __name__ == '__main__':

    sim_key = '564f3d60-c1a5-4f4d-ba21-1dbf08a532d5'
    distance = 50
    with DroneBlocksSimulatorContextManager(simulator_key=sim_key) as drone:
        # Despegar
        drone.takeoff()
        # Adelante y a la derecha
        drone.fly_forward(distance, 'cm')
        drone.fly_right(distance, 'cm')
        # Adelante y a la izquierda
        drone.fly_forward(distance, 'cm')
        drone.fly_left(distance, 'cm')
        # Adelante y a la derecha
        drone.fly_forward(distance, 'cm')
        drone.fly_right(distance, 'cm')
        # Adelante y a la izquierda
        drone.fly_forward(distance, 'cm')
        drone.fly_left(1.5*distance, 'cm')
        # Regresar al punto de despegue
        drone.fly_backward(4*distance, 'cm')
        drone.fly_right(0.5*distance, 'cm')
        # Aterrizar
        drone.land()