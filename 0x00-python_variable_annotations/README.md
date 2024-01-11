Python Variable Annotations

Variable annotations in Python allow you to provide additional information
about variables, enhancing code readability and providing hints to tools like
linters and type checkers. Introduced in Python 3.7, variable annotations are
distinct from variable assignments and can be used with type hints.

Syntax:
variable_name: annotation

Here, annotation can be any valid expression.

Example:
# Basic variable annotation
age: int = 25

# Variable annotation with a complex type hint
coordinates: Tuple[float, float] = (10.0, 20.0)

# Variable annotation with a custom class
class Person:
    name: str
    age: int

# Function parameter annotation
def greet(name: str) -> None:
    print(f"Hello, {name}!")

# Type hint for a dictionary
person_info: Dict[str, Union[str, int]] = {'name': 'John', 'age': 30}
