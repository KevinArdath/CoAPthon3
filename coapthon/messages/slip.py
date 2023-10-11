__author__ = 'Kevin Ardath'

""" SLIP Bytes """
END = b'\xC0'
ESC = b'\xDB'
ESC_END = b'\xDC'
ESC_ESC = b'\xDD'

def slip_encode(message):
    """
    Escapes SLIP ESC and END bytes and wraps the message in SLIP bytes

    :param message: a fully encoded COAP byte array
    :return: the slip encoded message
    :rtype: bytearray
    """
    return END + message.replace(ESC, ESC + ESC_ESC).replace(END, ESC + ESC_END) + END


def slip_decode(message):
    """
    Removes SLIP bytes and decodes escaped SLIP ESC and END bytes

    :param message: a slip encoded COAP response message
    :return: the raw message
    :rtype: bytearray
    """
    return message.strip(END).replace(ESC + ESC_END, END).replace(ESC + ESC_ESC, ESC)
