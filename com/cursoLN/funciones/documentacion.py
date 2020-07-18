import inspect

# from factorial import factorial_calc
import com.sci.funciones.factorial

method_list = [func[0] for func in inspect.getmembers(com.sci.funciones.factorial, predicate=inspect.isroutine) if callable(getattr(com.sci.funciones.factorial, func[0]))]