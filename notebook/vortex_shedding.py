def calcVortexSheddingFreq(Cd_data,Cl_data,time,h_beam,u_mid_beam):
    
    import numpy as np
    import scipy.signal as signal
    import matplotlib.pyplot as plt
    
    N = len(time)
    dt = time[2] - time[1]
    
    nmax=512 # no. of points in the fft
    freq, Cl_amp = signal.welch(Cl, 1./dt, nperseg=nmax)
    Cl_max_fft_idx = np.argmax(abs(Cl_amp))  
    freq_shed      = freq[Cl_max_fft_idx ] # Vortex shedding freq [Hz]
    St             = freq_shed * h_beam / u_mid_beam
    
    
    return freq, Cl_amp, St

