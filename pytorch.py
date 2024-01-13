# Para empezar a trabajar con pytorch tengo que importarlo.
# Previamente debo instalarlo por terminal: pip install torch torchvision

import torch

# Creo un tensor de rango 1 (vector)
tensor_1d = torch.tensor([1, 2, 3])

# Operaciones básicas: SUMA
result = tensor_1d + tensor_1d
print(result)
# Devolverá : [2, 4, 6]