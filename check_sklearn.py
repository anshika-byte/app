try:
    import sklearn
    print("scikit-learn is installed")
except ImportError:
    print("scikit-learn is not installed")
import sys
print(sys.executable)
