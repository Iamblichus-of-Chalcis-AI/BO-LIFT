from .version import __version__
from .asktell import AskTellFewShotMulti, AskTellFewShotTopk
from .asktellfinetuning import AskTellFinetuning

try:
    from .asktellGPR import AskTellGPR
    from .asktellRidgeRegression import AskTellRidgeKernelRegression
except ImportError:
    print("GPR Packages not installed. Do `pip install bolift[gpr]` to install them")
from .asktellNearestNeighbor import AskTellNearestNeighbor
from .pool import Pool
from .tool import BOLiftTool
