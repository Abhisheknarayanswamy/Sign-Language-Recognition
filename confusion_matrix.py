import numpy
from sklearn.metrics import confusion_matrix
expected=[green,green,opaque,opaque,red,red,yellow,yellow]
predicted=[green,green,opaque,opaque,red,red,yellow,yellow]
results=confusion_matrix(expected,predicted)
print(results)