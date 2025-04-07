from backend.services import MathEngine
from backend.services import Expression_prossesor

input = "1+1"

processor = Expression_prossesor(input)
engine = MathEngine(processor.get_inner_expression(), processor.mode)

print(engine.evaluate())
