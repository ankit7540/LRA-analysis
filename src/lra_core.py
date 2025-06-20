import numpy as np
#------------------------

def SNR_cutoff( xaxis , matrix, nComponents):
    
    # Perform singular value decomposition (SVD)
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)
    
    snrE = compute_snr_eVec(matrix, nComponents + 6)
    vecIndex =  snrE[:,0] 
    SNR = (snrE[:,1]+snrE[:,2]+snrE[:,3]+snrE[:,4]) / 4
    
    
    print('\t SNR : ',SNR)
    cutoff = analyze_SNR_U( SNR )
    print("\t Determined auto-cutoff (based on SNR) : ", cutoff )    
    
    return cutoff


#------------------------
#----------------------------------------------------------------
from scipy.signal import savgol_filter

def compute_snr_eVec(matrix, last_rank):
    # Perform singular value decomposition (SVD)
    U, S, Vt = np.linalg.svd(matrix, full_matrices=False)    
    
    out = np.zeros((last_rank,5))
    
    for i in range(out.shape[0]):
        out[i,0] = i+1
        out[i,1] = compute_SNR( U[:,i] , 5 , 2 )
        out[i,2] = compute_SNR( U[:,i] , 7 , 3 )
        out[i,3] = compute_SNR( U[:,i] , 9 , 4 )
        out[i,4] = compute_SNR( U[:,i] , 11 , 5 )
    
    return out
    
#----------------------------------------------------------------
#----------------------------------------------------------------

def compute_SNR(vector1D, window, pol):
    
    # Calculate smoothed values with Savitzky-Golay method
    smoothed = savgol_filter( vector1D, window_length=window, polyorder=pol)
    
    noise = vector1D - smoothed
    
    sdev_signal = np.std(smoothed)
    sdev_noise = np.std(noise)
    
    return (sdev_signal / sdev_noise )

#----------------------------------------------------------------
#----------------------------------------------------------------

def analyze_SNR_U( SNRavg ):
    
    # 1D vector = SNRavg
    
    cutOff = 2
    
    dim = SNRavg.shape[0]
    for i in range(dim):
        
        if (SNRavg[i] > 0.98) :
            cutOff = i
        else:
            cutOff = i - 1
            break
    
    return cutOff+1   # since counting from 1

#----------------    