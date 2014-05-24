

from numpy import *
import matplotlib.pylab as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__=='__main__':

    #Heat Equation Solver modeled after A Survey of Computational Physics

    #Initiate variables
    Nx=101; Nt= 10000; Dx=0.03; Dt=2
    KAPPA =230.; SPH=900.;
    RHO= 2700.

    T= zeros((Nx,2),float); Tpl=zeros((Nx,31),float)

    print ("Working, wait for figure")

    for ix in range(1,Nx-1):
        T[ix,0]=100;
        T[0,0]=0.0;T[0,1]=0.
        T[Nx - 1,0]=0.; T[Nx - 1,1]=0.0;
        cons=KAPPA/(SPH*RHO)*Dt/(Dx*Dx);
        m=1

    for t in range(1, Nt):
        for ix in range(1, Nx -1):
            T[ix,1]=T[ix,0] + cons*(T[ix + 1,0 ]  +T[ix - 1,0] - 2.*T[ix,0])
        if t%500 == 0 or t==1:
            for ix in range (1,Nx -1, 2): Tpl[ix,m]=T[ix,1]
            
            m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]

    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)

    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r')
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('1.Heat Equation Numerical')
    plt.show()
    print('finished')

    

    #Define a 2-D array T[101][2] for the temperature as a function of space and time. The
    #first index is for the 100 space divisions of the bar, and the second index is for present and
    #past times (because you may have to make thousands of time steps, you save memory by
    #saving only two times).


    ##Analytical Solution
    
    m=0

    def Heat(b,t):
        summ=0.
        cons=KAPPA/(SPH*RHO)
        L=101.
        for n in range(1,10000,2):
            kn=(n*3.14)/L
            summ=summ+((4*T0)/(n*3.14))*np.sin(kn*b)*np.exp(-(kn**2)*cons*t)
        return summ


    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)


    Tpl=zeros((Nx,31),float)
    T= zeros((Nx,2),float)

    print('Working, wait for figure')
    for t in range(1, 10000000,400000):
        if t==1: T0=100.
        for ix in range (1,Nx -1, 2): Tpl[ix,m]=Heat(ix,t)
        
        m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]


    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)

    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r', cmap=cm.coolwarm)
    cset= ax.contour(X,Y,Z, zdir='z', offset= -pi, cmap=cm.coolwarm)
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('2.Heat Equation Analytical')
    plt.show()
    print('finished')

    

    #######################

    #Plotting 3d color map XYZ DATA

    fig = plt.figure(figsize=(8,6))

    ax = fig.add_subplot(1,1,1, projection='3d')

    p=ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.jet)
    cset = ax.contour(X, Y, Z, zdir='z', cmap=cm.jet)
    cset = ax.contour(X, Y, Z, zdir='x', cmap=cm.jet)
    cset = ax.contour(X, Y, Z, zdir='y', cmap=cm.jet)
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('3.Heat Equation Heatmap')
    cb = fig.colorbar(p, shrink=0.5)


    #Stability test
    Nx=101; Nt= 10000; Dx=0.03; Dt=3.8
    

    T= zeros((Nx,2),float); Tpl=zeros((Nx,31),float)

    print ("Working, wait for figure")

    for ix in range(1,Nx-1):
        T[ix,0]=100;
        T[0,0]=0.0;T[0,1]=0.
        T[Nx - 1,0]=0.; T[Nx - 1,1]=0.0;
        #Changed from .21
        cons=.51
        m=1

    for t in range(1, Nt):
        for ix in range(1, Nx -1):
            T[ix,1]=T[ix,0] + cons*(T[ix + 1,0 ]  +T[ix - 1,0] - 2.*T[ix,0])
        if t%500 == 0 or t==1:
            for ix in range (1,Nx -1, 2): Tpl[ix,m]=T[ix,1]
            
            m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]

    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)

    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r')
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('4.Heat Equation Stability')
    plt.show()
    print('finished')

    ### Calculation for an Iron Bar
    Nx=101; Nt= 10000; Dx=0.03; Dt=4.8
    KAPPA =80.; SPH=450.;
    RHO= 7874.

    T= zeros((Nx,2),float); Tpl=zeros((Nx,31),float)

    print ("Working, wait for figure")

    for ix in range(1,Nx-1):
        T[ix,0]=100;
        T[0,0]=0.0;T[0,1]=0.
        T[Nx - 1,0]=0.; T[Nx - 1,1]=0.0;
        #Changed from .21
        cons=.26
        m=1

    for t in range(1, Nt):
        for ix in range(1, Nx -1):
            T[ix,1]=T[ix,0] + cons*(T[ix + 1,0 ]  +T[ix - 1,0] - 2.*T[ix,0])
        if t%500 == 0 or t==1:
            for ix in range (1,Nx -1, 2): Tpl[ix,m]=T[ix,1]
            
            m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]

    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)

    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r')
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('5.Heat Equation Iron Bar')
    plt.show()
    print('finished')



    #### Analytical sin solution approximation 

    
    m=0

    def Heat(b,t):
        summ=0.
        cons=KAPPA/(SPH*RHO)
        L=101.
        summ = np.sin(3.14*b/L)*np.exp(-(3.14**2)*cons*t*(1/(L**2)))
        return summ


    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)


    Tpl=zeros((Nx,31),float)
    T= zeros((Nx,2),float)

    print('Working, wait for figure')
    for t in range(1, 10000000,400000):
        if t==1: T0=100.
        for ix in range (1,Nx -1, 2): Tpl[ix,m]=Heat(ix,t)
        
        m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]


    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)

    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r', cmap=cm.coolwarm)
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('6.Sin Approximation')
    plt.show()
    print('finished')

    ##Two bars at different temperatures.

    Nx=101; Nt= 10000; Dx=0.03; Dt=2
    KAPPA =230.; SPH=900.;
    RHO= 2700.

    T= zeros((Nx,2),float); Tpl=zeros((Nx,31),float)

    print ("Working, wait for figure")

    for ix in range(1,Nx-1):
        if ix < Nx/2:T[ix,0]=100;
        if ix > Nx/2:T[ix,0]=50;
        if ix == Nx/2:T[ix,0]=75;
        T[0,0]=0.0;T[0,1]=0.
        T[Nx - 1,0]=0.; T[Nx - 1,1]=0.0;
        cons=KAPPA/(SPH*RHO)*Dt/(Dx*Dx);
        m=1

    for t in range(1, Nt):
        for ix in range(1, Nx -1):
            T[ix,1]=T[ix,0] + cons*(T[ix + 1,0 ]  +T[ix - 1,0] - 2.*T[ix,0])
        if t%500 == 0 or t==1:
            for ix in range (1,Nx -1, 2): Tpl[ix,m]=T[ix,1]
            
            m=m+1
        for ix in range(1, Nx -1 ): T[ix,0]=T[ix,1]

    x=list(range(1, Nx - 1 ,2))
    y=list(range(1,30))
    X,Y = plt.meshgrid(x,y)

    def functz(Tpl):
        z=Tpl[X,Y]
        return z

    Z=functz(Tpl)
    fig=plt.figure()
    ax=Axes3D(fig)
    ax.plot_wireframe(X,Y,Z, color='r')
    cset= ax.contour(X,Y,Z, zdir='z', offset= -pi, cmap=cm.coolwarm)
    ax.set_xlabel('position')
    ax.set_ylabel('time')
    ax.set_zlabel('temp')
    ax.set_title('7.Heat Eq Two Bars in Contact')
    plt.show()
    print('finished')
