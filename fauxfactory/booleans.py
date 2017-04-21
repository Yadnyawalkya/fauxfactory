"""Method for generating random boolean values."""

from fauxfactory.choices import gen_choice


def gen_boolean():
    """Return a random Boolean value.

    :returns: A random Boolean value.
    :rtype: bool

    """
    choices = (True, False)

    return gen_choice(choices)
