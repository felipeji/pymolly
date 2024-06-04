# A toy classs for showing Teo
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def introduce(self):
    print("Hello my name is " + self.name)
    print('I am ' + str (self.age) + ' years old.')



# Example: the fits module and the class PrimaryHDU (Astropy)
from astropy.io import fits 

path_image = '/Users/felipe/Desktop/Aladin_cutout/aladin_ALLBRICQSJ1904.fits'
image = fits.open(path_image)






#  Molly Class

# Dependencies (trm + astropy +matplotlib)
from trm.molly import rmolly
import matplotlib.pyplot as plt
from astropy import units as u
from specutils.spectra import Spectrum1D, SpectralRegion
from specutils.fitting import fit_generic_continuum


# Function for reading .mol into wave, flux and header variables

def read_molly(file, index):
    wave = rmolly(file)[index].wave
    flux = rmolly(file)[index].f
    header = rmolly(file)[index].head

    return wave, flux, header


# Read a slot in a  .mol file 
path = '/Users/felipe/LMXBs/4_MAXIJ1820+070-BOWEN/0_dotmol_clip/1_OSIRIS_phase_clip_move_R2500V.mol'
wave, flux, header= read_molly(path,3)




# ======================================================
#  Example structure (A)
# ======================================================


class Molly:
  def __init__(self, wave, flux, header):
    self.wave = wave
    self.flux = flux
    self.header = header

  def normalize(self, mask = None):
    
    # If no mask is set, take default values
    if mask is None:    
        mask = SpectralRegion(4615*u.Angstrom, 4720*u.Angstrom) + SpectralRegion(4830*u.Angstrom, 4890*u.Angstrom) 
    
    spectrum = Spectrum1D(spectral_axis=self.wave *u.Angstrom, flux=self.flux * u.Jy )
    norm_fitting = fit_generic_continuum(spectrum, exclude_regions=mask)
    normalization = norm_fitting( self.wave * u.Angstrom)

    norm_flux = self.flux/normalization.value

    return self.wave, norm_flux, normalization.value


m = Molly(wave, flux, header)




# # ======================================================
# #  Example structure (B)
# # ======================================================


# class Molly:
#   def __init__(self, wave, flux, header):
#     self.wave = wave
#     self.flux = flux
#     self.header = header

#     # Normalize the spectra
#     # The list with all the masked regions    
#     mask = SpectralRegion(4615*u.Angstrom, 4720*u.Angstrom) + SpectralRegion(4830*u.Angstrom, 4890*u.Angstrom) 
#     # Set Normalizatio fitting function and parameters
#     spectrum = Spectrum1D(spectral_axis=self.wave *u.Angstrom, flux=self.flux * u.Jy )
#     norm_fitting = fit_generic_continuum(spectrum, exclude_regions=mask)
#     # Normalization fitting
#     continuun_fit = norm_fitting( self.wave * u.Angstrom)

#     self.continuun = continuun_fit.value
#     self.normalized = self.flux/self.continuun


#   def plot(self, norm = False):
#     # Plot normalized spectrum?
#     if norm:
#       f = self.normalized
#     else:
#       f = self.flux

#     # Set figure
#     plt.plot(self.wave, f)  


    
# m = Molly(wave, flux, header)



# # Molly reader (multiple slots readed into a lis of Molly intances)

# def load_molly(path):
#   dotmol = rmolly(path)
#   list = []
#   for i in dotmol:
#     wave = i.wave
#     flux = i.f
#     header = i.head
#     molly = Molly(wave, flux, header)
#     list.append(molly)

#   return list
    

# mollys = load_molly(path)



# # Example: executiion of the same method over the whole list
# plt.close('all')

# for m in mollys:
#   m.plot(norm=True)

# plt.ion(),plt.show()
