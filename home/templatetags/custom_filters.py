# templatetags/math_tags.py

import random
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """Multiply the value by the argument."""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def mod(value, arg):
    """Return the modulo of value divided by arg."""
    try:
        return int(value) % int(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

@register.filter
def divide(value, arg):
    """Divide the value by the argument."""
    try:
        return int(value) // int(arg)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

@register.filter
def subtract(value, arg):
    """Subtract the argument from the value."""
    try:
        return int(value) - int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def add_custom(value, arg):
    """Add the argument to the value (alternative to built-in add)."""
    try:
        return int(value) + int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def power(value, arg):
    """Raise value to the power of arg."""
    try:
        return int(value) ** int(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def abs_value(value):
    """Return the absolute value."""
    try:
        return abs(int(value))
    except (ValueError, TypeError):
        return 0

@register.filter
def min_value(value, arg):
    """Return the minimum of value and arg."""
    try:
        return min(int(value), int(arg))
    except (ValueError, TypeError):
        return 0

@register.filter
def max_value(value, arg):
    """Return the maximum of value and arg."""
    try:
        return max(int(value), int(arg))
    except (ValueError, TypeError):
        return 0

@register.filter
def range_filter(value):
    """Create a range from 0 to value-1."""
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(0)

@register.filter
def to_int(value):
    """Convert value to integer."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0

@register.filter
def to_float(value):
    """Convert value to float."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0

# More complex calculations for common use cases
@register.filter
def animation_delay(counter):
    """Calculate animation delay based on counter (counter * 100)."""
    try:
        return int(counter) * 100
    except (ValueError, TypeError):
        return 0

@register.filter
def gradient_class(counter):
    """Calculate gradient class number (1-6) based on counter."""
    try:
        return ((int(counter) + 6) % 6) + 1
        # return random.randint(1, 6)
    except (ValueError, TypeError):
        return 1

@register.filter
def star_range(rating):
    """Create a range for star ratings (1 to 5)."""
    try:
        return range(1, 6)  # Always 1-5 for star ratings
    except:
        return range(1, 6)

@register.filter
def is_filled_star(star_num, rating):
    """Check if a star should be filled based on rating."""
    try:
        return int(star_num) <= int(rating)
    except (ValueError, TypeError):
        return False

# Simple tag for mathematical operations
@register.simple_tag
def calculate(value, operation, operand):
    """
    Perform mathematical operations.
    Usage: {% calculate forloop.counter0 'multiply' 100 %}
    """
    try:
        value = float(value)
        operand = float(operand)
        
        if operation == 'multiply' or operation == 'mul':
            return int(value * operand)
        elif operation == 'divide' or operation == 'div':
            return int(value / operand) if operand != 0 else 0
        elif operation == 'add':
            return int(value + operand)
        elif operation == 'subtract' or operation == 'sub':
            return int(value - operand)
        elif operation == 'mod' or operation == 'modulo':
            return int(value % operand) if operand != 0 else 0
        elif operation == 'power' or operation == 'pow':
            return int(value ** operand)
        else:
            return int(value)
    except (ValueError, TypeError, ZeroDivisionError):
        return 0

# Inclusion tag for complex calculations
@register.inclusion_tag('tags/math_result.html')
def math_operation(value1, operation, value2):
    """
    Complex mathematical operations with template rendering.
    """
    try:
        val1 = float(value1)
        val2 = float(value2)
        
        operations = {
            'add': val1 + val2,
            'subtract': val1 - val2,
            'multiply': val1 * val2,
            'divide': val1 / val2 if val2 != 0 else 0,
            'mod': val1 % val2 if val2 != 0 else 0,
            'power': val1 ** val2,
        }
        
        result = operations.get(operation, 0)
        
        return {
            'result': int(result),
            'value1': val1,
            'value2': val2,
            'operation': operation
        }
    except (ValueError, TypeError, ZeroDivisionError):
        return {
            'result': 0,
            'value1': 0,
            'value2': 0,
            'operation': operation
        }

# Helper functions for common template patterns
@register.filter
def get_item(dictionary, key):
    """Get item from dictionary by key."""
    try:
        return dictionary.get(key, '')
    except (AttributeError, TypeError):
        return ''

@register.filter
def get_index(list_obj, index):
    """Get item from list by index."""
    try:
        return list_obj[int(index)]
    except (IndexError, ValueError, TypeError):
        return ''

@register.filter
def percentage(value, total):
    """Calculate percentage."""
    try:
        return round((float(value) / float(total)) * 100, 2) if total != 0 else 0
    except (ValueError, TypeError, ZeroDivisionError):
        return 0