import math

def num_zeros(decimal: float) -> int:
    """
    @param decimal: a floating point number with an absolute value smaller than 1
    @return: the number of zeros trailing the decimal point before a non-zero digit is encountered
    """
    return math.inf if decimal == 0 else -math.floor(math.log10(abs(decimal))) - 1

def calc_significant_digits(err: float) -> int:
    """
    @param err: the error associated with some value
    @return: the appropriate number of significant digits after the decimal point of the value associated with err
    """
    significant_digits = num_zeros(err) + 1
    if significant_digits == num_zeros(round(err, significant_digits)) + 1:
        return significant_digits
    else:
        return significant_digits - 1

def format_num(val: float, n_digits: int) -> str:
    """
    @param val: a floating point number to be formatted
    @param n_digits: the number of digits to be retained after the decimal point
    @return: a string containing val formatted with n_digits number of digits trailing the decimal point
    """
    if n_digits == 0:
        return str(round(val))

    rounded_val = round(val, n_digits)
    val_str = format(rounded_val, f".{n_digits}f")
    return val_str


def format_num_with_err(val, err, parenthesis_error=False, do_add_dollars=False) -> str:
    """
    @param val: a measurement value
    @param err: the error associated with val
    @param parenthesis_error: denote errors inside parenthesis rather than using the standard \pm (+/-)
    @param do_add_dollars: adds $-signs to the beginning of end of the output if True (used in LaTeX formatting)
    @return: a string
    """
    if val < err:
        raise ValueError("The error is larger than the value itself")

    if val == "nan" or err == "nan":
        return "--"

    error_is_below_unity = True
    scale = 1

    if err >= 1:
        scale = 10**math.floor(math.log10(err))
        val /= scale
        err /= scale
        error_is_below_unity = False

    s_dig = calc_significant_digits(err)
    rounded_val = round(val, s_dig)
    rounded_err = round(err, s_dig)

    if error_is_below_unity:
        val_str = format_num(rounded_val, s_dig)
        err_str = ((f"({format_num(rounded_err*10**s_dig, 0)})" if parenthesis_error
                    else r"\pm " + format_num(rounded_err, s_dig)))
    else:
        val_str = str(round(rounded_val*scale))
        err_str = f"({round(rounded_err * scale)})" if parenthesis_error else r"\pm " + str(round(rounded_err * scale))

    out_str = f"{val_str} {err_str}"
    if do_add_dollars:
        out_str = f"${out_str}$"

    return out_str
