#Separation of variables in Laplace equation in spherical coordinates

In[1]:

.. code:: python

    r, phi, theta = symbols("r,phi,theta")
    Xi = Function('Xi')
    R, Phi, Theta, u = map(Function, ['R', 'Phi', 'Theta', 'u'])
    C1, C2 = symbols('C1,C2')
    D = Derivative


## Laplace equation in spherical coordinates:

In[2]:

.. code:: python

    eq = Eq(D(Xi(r, phi, theta), r, 2) + 2/r * D(Xi(r, phi, theta),r) + \
            1/(r**2 * sin(phi)**2) * D(Xi(r, phi, theta), theta, 2) + \
            cos(phi)/(r**2 * sin(phi)) * D(Xi(r, phi, theta), phi) + \
            1/r**2 * D(Xi(r, phi, theta), phi, 2))
    eq


Out[2]:

.. math::

    $$\frac{\partial^{2}}{\partial^{2} r}  \operatorname{Xi}{\left (r,\phi,\theta \right )} + 2 \frac{\frac{\partial}{\partial r} \operatorname{Xi}{\left (r,\phi,\theta \right )}}{r} + \frac{\frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{Xi}{\left (r,\phi,\theta \right )}}{r^{2}} + \frac{\cos{\left (\phi \right )} \frac{\partial}{\partial \phi} \operatorname{Xi}{\left (r,\phi,\theta \right )}}{r^{2} \sin{\left (\phi \right )}} + \frac{\frac{\partial^{2}}{\partial^{2} \theta}  \operatorname{Xi}{\left (r,\phi,\theta \right )}}{r^{2} \sin^{2}{\left (\phi \right )}} = 0$$

.. parsed-literal::

    
                                           2                                      
                                          d                                       
                        d                ───(Ξ(r, φ, θ))          d               
      2               2⋅──(Ξ(r, φ, θ))     2               cos(φ)⋅──(Ξ(r, φ, θ))  
     d                  dr               dφ                       dφ              
    ───(Ξ(r, φ, θ)) + ──────────────── + ─────────────── + ───────────────────── +
      2                      r                   2                2               
    dr                                          r                r ⋅sin(φ)        
    
       2                
      d                 
     ───(Ξ(r, φ, θ))    
       2                
     dθ                 
     ─────────────── = 0
         2    2         
        r ⋅sin (φ)      


We can either separate this equation in regards with variable r:

In[3]:

.. code:: python

    res_r = pde_separate(eq, Xi(r, phi, theta), [R(r), u(phi, theta)])
    res_r

Out[3]:

.. math::

    $$\begin{bmatrix}\frac{3}{2} \frac{r^{2} \frac{\partial^{2}}{\partial^{2} r}  \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}} + 3 \frac{r \frac{\partial}{\partial r} \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}}, & - \frac{3}{2} \frac{\frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{u}{\left (\phi,\theta \right )}}{\operatorname{u}{\left (\phi,\theta \right )}} - \frac{3}{2} \frac{\frac{\partial}{\partial \phi} \operatorname{u}{\left (\phi,\theta \right )}}{\operatorname{u}{\left (\phi,\theta \right )} \tan{\left (\phi \right )}} - \frac{3}{2} \frac{\frac{\partial^{2}}{\partial^{2} \theta}  \operatorname{u}{\left (\phi,\theta \right )}}{\operatorname{u}{\left (\phi,\theta \right )} \sin^{2}{\left (\phi \right )}}\end{bmatrix}$$

.. parsed-literal::

    [
           2                     
       2  d                      
    3⋅r ⋅───(R(r))       d       
           2         3⋅r⋅──(R(r))
         dr              dr      
    ────────────── + ────────────
        2⋅R(r)           R(r)    ,
     
          2                                     2          
         d                                     d           
      3⋅───(u(φ, θ))      d                 3⋅───(u(φ, θ)) 
          2             3⋅──(u(φ, θ))           2          
        dφ                dφ                  dθ           
    - ────────────── - ──────────────── - ─────────────────
        2⋅u(φ, θ)      2⋅u(φ, θ)⋅tan(φ)                2   
                                          2⋅u(φ, θ)⋅sin (φ)]


Or separate it in regards of theta:

In[4]:

.. code:: python

    res_theta = pde_separate(eq, Xi(r, phi, theta), [Theta(theta), u(r, phi)])
    res_theta

Out[4]:

.. math::

    $$\begin{bmatrix}\frac{\frac{\partial^{2}}{\partial^{2} \theta}  \operatorname{Theta}{\left (\theta \right )}}{\operatorname{Theta}{\left (\theta \right )}}, & - \frac{r^{2} \sin^{2}{\left (\phi \right )} \frac{\partial^{2}}{\partial^{2} r}  \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - 2 \frac{r \sin^{2}{\left (\phi \right )} \frac{\partial}{\partial r} \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - \frac{\sin^{2}{\left (\phi \right )} \frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - \frac{\sin{\left (\phi \right )} \cos{\left (\phi \right )} \frac{\partial}{\partial \phi} \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}}\end{bmatrix}$$

.. parsed-literal::

    [
      2      
     d       
    ───(Θ(θ))
      2      
    dθ       
    ─────────
       Θ(θ)  ,
     
                   2                                                2             
       2    2     d                                          2     d              
      r ⋅sin (φ)⋅───(u(r, φ))          2    d             sin (φ)⋅───(u(r, φ))    
                   2            2⋅r⋅sin (φ)⋅──(u(r, φ))             2            s
                 dr                         dr                    dφ              
    - ─────────────────────── - ─────────────────────── - ──────────────────── - ─
              u(r, φ)                   u(r, φ)                 u(r, φ)           
    
                            
                            
                 d          
    in(φ)⋅cos(φ)⋅──(u(r, φ))
                 dφ         
    ────────────────────────
            u(r, φ)         ]


But we cannot separate it in regards of variable phi:

In[5]:

.. code:: python

    res_phi = pde_separate(eq, Xi(r, phi, theta), [Phi(phi), u(r, theta)])
    res_phi


In[6]:

.. code:: python

    res_phi is None

Out[6]:

.. parsed-literal::

    True


So let's make theta dependent part equal with -C1:

In[7]:

.. code:: python

    eq_theta = Eq(res_theta[0], -C1)
    eq_theta

Out[7]:

.. math::

    $$\frac{\frac{\partial^{2}}{\partial^{2} \theta}  \operatorname{Theta}{\left (\theta \right )}}{\operatorname{Theta}{\left (\theta \right )}} = - C_{1}$$

.. parsed-literal::

    
      2            
     d             
    ───(Θ(θ))      
      2            
    dθ             
    ───────── = -C₁
       Θ(θ)        


This also means that second part is also equal to -C1:

In[8]:

.. code:: python

    eq_left = Eq(res_theta[1], -C1)
    eq_left

Out[8]:

.. math::

    $$- \frac{r^{2} \sin^{2}{\left (\phi \right )} \frac{\partial^{2}}{\partial^{2} r}  \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - 2 \frac{r \sin^{2}{\left (\phi \right )} \frac{\partial}{\partial r} \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - \frac{\sin^{2}{\left (\phi \right )} \frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} - \frac{\sin{\left (\phi \right )} \cos{\left (\phi \right )} \frac{\partial}{\partial \phi} \operatorname{u}{\left (r,\phi \right )}}{\operatorname{u}{\left (r,\phi \right )}} = - C_{1}$$

.. parsed-literal::

    
                   2                                                2             
       2    2     d                                          2     d              
      r ⋅sin (φ)⋅───(u(r, φ))          2    d             sin (φ)⋅───(u(r, φ))    
                   2            2⋅r⋅sin (φ)⋅──(u(r, φ))             2            s
                 dr                         dr                    dφ              
    - ─────────────────────── - ─────────────────────── - ──────────────────── - ─
              u(r, φ)                   u(r, φ)                 u(r, φ)           
    
                                  
                                  
                 d                
    in(φ)⋅cos(φ)⋅──(u(r, φ))      
                 dφ               
    ──────────────────────── = -C₁
            u(r, φ)               


Lets try to separate phi again:

In[9]:

.. code:: python

    res_theta = pde_separate(eq_left, u(r, phi), [Phi(phi), R(r)])
    res_theta

Out[9]:

.. math::

    $$\begin{bmatrix}- \frac{C_{1}}{\sin^{2}{\left (\phi \right )}} + \frac{\frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{Phi}{\left (\phi \right )}}{\operatorname{Phi}{\left (\phi \right )}} + \frac{\cos{\left (\phi \right )} \frac{\partial}{\partial \phi} \operatorname{Phi}{\left (\phi \right )}}{\operatorname{Phi}{\left (\phi \right )} \sin{\left (\phi \right )}}, & - \frac{r^{2} \frac{\partial^{2}}{\partial^{2} r}  \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}} - 2 \frac{r \frac{\partial}{\partial r} \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}}\end{bmatrix}$$

.. parsed-literal::

    [
                  2                        
                 d                         
                ───(Φ(φ))          d       
                  2         cos(φ)⋅──(Φ(φ))
         C₁     dφ                 dφ      
    - ─────── + ───────── + ───────────────
         2         Φ(φ)       Φ(φ)⋅sin(φ)  
      sin (φ)                              ,
     
           2                     
       2  d                      
      r ⋅───(R(r))       d       
           2         2⋅r⋅──(R(r))
         dr              dr      
    - ──────────── - ────────────
          R(r)           R(r)    ]


This time it is successful.

## So our final equations with separated variables are:

In[10]:

.. code:: python

    eq_theta

Out[10]:

.. math::

    $$\frac{\frac{\partial^{2}}{\partial^{2} \theta}  \operatorname{Theta}{\left (\theta \right )}}{\operatorname{Theta}{\left (\theta \right )}} = - C_{1}$$

.. parsed-literal::

    
      2            
     d             
    ───(Θ(θ))      
      2            
    dθ             
    ───────── = -C₁
       Θ(θ)        


In[11]:

.. code:: python

    Eq(res_theta[0],C2)

Out[11]:

.. math::

    $$- \frac{C_{1}}{\sin^{2}{\left (\phi \right )}} + \frac{\frac{\partial^{2}}{\partial^{2} \phi}  \operatorname{Phi}{\left (\phi \right )}}{\operatorname{Phi}{\left (\phi \right )}} + \frac{\cos{\left (\phi \right )} \frac{\partial}{\partial \phi} \operatorname{Phi}{\left (\phi \right )}}{\operatorname{Phi}{\left (\phi \right )} \sin{\left (\phi \right )}} = C_{2}$$

.. parsed-literal::

    
                  2                             
                 d                              
                ───(Φ(φ))          d            
                  2         cos(φ)⋅──(Φ(φ))     
         C₁     dφ                 dφ           
    - ─────── + ───────── + ─────────────── = C₂
         2         Φ(φ)       Φ(φ)⋅sin(φ)       
      sin (φ)                                   


In[12]:

.. code:: python

    Eq(res_theta[1],C2)

Out[12]:

.. math::

    $$- \frac{r^{2} \frac{\partial^{2}}{\partial^{2} r}  \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}} - 2 \frac{r \frac{\partial}{\partial r} \operatorname{R}{\left (r \right )}}{\operatorname{R}{\left (r \right )}} = C_{2}$$

.. parsed-literal::

    
           2                          
       2  d                           
      r ⋅───(R(r))       d            
           2         2⋅r⋅──(R(r))     
         dr              dr           
    - ──────────── - ──────────── = C₂
          R(r)           R(r)         

