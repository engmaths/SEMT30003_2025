#!/usr/bin/python
# -*- coding: UTF-8 -*-

# Create Matlab-like namespace
from pylab import *

class HH_model:
    # enclose parameters in an object without having to
    # unpack everything from `self` in instance methods.
    def __init__(self,
        # Potassium voltage gating (open/close) "n"
        KVth   = 25   , # K⁺  open threshold voltage (mV)
        Kr     = 9    , # K⁺  voltage gating scaling (mV)
        K_a    = 0.020, # K⁺  open  rate constant    (1/ms)
        K_b    = 0.002, # K⁺  close rate constant    (1/ms)
        # Sodium voltage gating (open/close) "m"
        NaVth  = -35  , # Na⁺ open threshold voltage (mV)
        Na_a   = 0.182, # Na⁺ open  rate constant    (1/ms)
        Na_b   = 0.124, # Na⁺ close rate constant    (1/ms)
        Nar    = 9    , # Na⁺ voltage gating scaling (mV)
        # Sodium voltage gating (inactivate/deinactivate) "h"
        HVin1  = -62  , # Na⁺ inactivation threshold (mV)
        Hr1    =   6  , # Na⁺ inactivation scale     (mV)
        HVin2  = -90  , # Na⁺ deinactivation voltage (mV)
        Hr2    =  12  , # Na⁺ deinactivation scale   (mV)
        H_k    = .25  , # Na⁺ activation rate        (1/ms)
        # Specific maximal conductances
        gL     = 0.3  , # Leak conductance    (millisiemens/cm²)
        gKmax  = 35   , # K⁺  max conductance (millisiemens/cm²)
        gNamax = 45   , # Na⁺ max conductance (millisiemens/cm²)
        # Reversal potentials
        EL     = -65  , # Leak reversal potential (mV)
        EK     = -77  , # K⁺   reversal potential (mV)
        ENa    =  55  , # Na⁺  reversal potential (mV)
        # Membrane specific capacitence
        C      = 1.0 ): # Membrane capacitance (microfarads /cm²)
        
        # exp clipped to avoid under/overflow
        exp  = lambda x  :np.exp(np.clip(x,-15,15)) 
        
        # Remove singularity from n,m gates
        gate = lambda x,r:np.where(x != 0, x / (1 - exp(-x / r)), r)
        
        # α/β rate forms of n,m,h gates
        an   = lambda v: K_a *gate(  v-KVth  ,Kr )
        bn   = lambda v: K_b *gate(-(v-KVth ),Kr )
        am   = lambda v: Na_a*gate(  v-NaVth ,Nar)
        bm   = lambda v: Na_b*gate(-(v-NaVth),Nar)
        ah   = lambda v: H_k * exp(-(v-HVin2)/Hr2)
        bh   = lambda v: ah(v)*exp( (v-HVin1)/Hr1)
        
        # Current as a function of voltage, gates
        def currents(v,m,n,h):
            sK  = n**4
            sNa = m**3*h    
            gK  = gKmax *sK
            gNa = gNamax*sNa
            IL  = gL *(EL -v)
            IK  = gK *(EK -v)
            INa = gNa*(ENa-v)
            return np.array([IL, IK, INa])
            
        # System ODE with input current I
        def ode(v,m,n,h,I):
            IL, IK, INa = self.currents(v,m,n,h)
            dv = (IK + INa + IL + I)/C
            dm = (1-m)*am(v) - bm(v)*m
            dn = (1-n)*an(v) - bn(v)*n
            dh = (1-h)*ah(v) - bh(v)*h
            return np.array([dv,dm,dn,dh])
            
        # Make everything above accessible in the object
        self.__dict__.update(locals())





    
