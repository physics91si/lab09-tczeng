# Physics 91SI
# Spring 2018
# Lab 8

# Modules you won't need
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Modules you will need
import numpy as np
import particle
import molecule as mc

# TODO: Implement this function
def init_molecule():
    molec = mc.Molecule(0.2, 0.2, 1, 0.8, 0.8, 2, 1, 0.5)
    return molec

# TODO: Implement this function
def time_step(dt, molec):
    """Sets new positions and velocities of the particles attached to mol"""
    # change velocity after incrementing by 0.5 dt
    molec.p1.vel[0] = molec.p1.vel[0] + (-molec.get_force()[0]/molec.p1.m)*0.5*dt
    molec.p1.vel[1] = molec.p1.vel[1] + (-molec.get_force()[1]/molec.p1.m)*0.5*dt
    
    molec.p2.vel[0] = molec.p2.vel[0] + (molec.get_force()[0]/molec.p2.m)*0.5*dt
    molec.p2.vel[1] = molec.p2.vel[1] + (molec.get_force()[1]/molec.p2.m)*0.5*dt
    
    # change position after incrementing by 1 dt
    molec.p1.pos[0] = molec.p1.pos[0] + molec.p1.vel[0]*dt
    molec.p1.pos[1] = molec.p1.pos[1] + molec.p1.vel[1]*dt
    molec.p2.pos[0] = molec.p2.pos[0] + molec.p2.vel[0]*dt
    molec.p2.pos[1] = molec.p2.pos[1] + molec.p2.vel[1]*dt
    
    

#############################################
# The rest of the file is already implemented
#############################################

def run_dynamics(n, dt, xlim=(0, 1), ylim=(0, 1)):
    """Calculate each successive time step and animate it"""
    mol = init_molecule()

    # Animation stuff
    fig, ax = plt.subplots()
    line, = ax.plot((mol.p1.pos[0], mol.p2.pos[0]), (mol.p1.pos[1], mol.p2.pos[1]), '-o')
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.xlabel(r'$x$')
    plt.ylabel(r'$y$')
    plt.title('Dynamics simulation')
    dynamic_ani = animation.FuncAnimation(fig, update_anim, n,
            fargs=(dt, mol,line), interval=50, blit=False)
    plt.show()

def update_anim(i,dt, mol,line):
    """Update and draw the molecule. Called by FuncAnimation"""
    time_step(dt, mol)
    line.set_data([(mol.p1.pos[0], mol.p2.pos[0]),
                   (mol.p1.pos[1], mol.p2.pos[1])])
    return line,

if __name__ == '__main__':
    # Set the number of iterations and time step size
    n = 10
    dt = .1
    run_dynamics(n, dt)
