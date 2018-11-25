import os.path
import sys

FILE_BUFFER_SIZE = 2 ** 20  # 2 or greater and even

HELP_TEXT = """\
RLE encoder/decoder by Kalle (http://qalle.net).
Command line arguments: MODE SOURCE_FILE TARGET_FILE
MODE
    E   encode
    D   decode
    This argument is case-insensitive.
SOURCE_FILE
    File to read.
TARGET_FILE
    File to write.
    The file must not already exist (it will not be overwritten)."""

def _read_file_in_chunks(handle):
    """Yield file contents in chunks of FILE_BUFFER_SIZE bytes or less."""
    bytesLeft = handle.seek(0, 2)
    handle.seek(0)

    while bytesLeft > 0:
        chunkSize = min(bytesLeft, FILE_BUFFER_SIZE)
        yield handle.read(chunkSize)
        bytesLeft -= chunkSize

def RLE_encode(handle):
    """Yield file contents as encoded RLE runs (length, byte)."""
    runByte = None
    runLen = None

    for chunk in _read_file_in_chunks(handle):
        for byte in chunk:
            if runByte is None:
                # first byte of first chunk
                runByte = byte
                runLen = 1
            elif byte != runByte or runLen == 255:
                # end of run; save it and start a new one
                yield (runLen, runByte)
                runByte = byte
                runLen = 1
            else:
                runLen += 1

    if runByte is not None:
        # save last data chunk
        yield (runLen, runByte)

    # end-of-file chunk (length 0, byte has no effect)
    yield bytes((0, 0x69))

def RLE_decode(handle):
    """Yield file contents as decoded RLE runs (length, byte)."""
    EOF = False

    for chunk in _read_file_in_chunks(handle):
        for pos in range(0, len(chunk), 2):
            try:
                (runLen, runByte) = chunk[pos:pos+2]
            except IndexError:
                exit("Error: RLE file size must be even.")
            if runLen == 0:
                EOF = True
                break
            yield (runLen, runByte)
        if EOF:
            break

    if not EOF:
        exit("Error: EOF missing.")

def compress(source, destination):
    with open(source, "rb") as sourceHnd, open(destination, "wb") as targetHnd:
        for (runLen, runByte) in RLE_encode(sourceHnd):
            targetHnd.write(bytes((runLen, runByte)))
    return destination

def decompress(compressed, decompressed):
    with open(compressed, "rb") as sourceHnd, open(decompressed, "wb") as targetHnd:
        for (runLen, runByte) in RLE_decode(sourceHnd):
            targetHnd.write(runLen * bytes((runByte,)))
    return decompressed

def main():
    # parse arguments
    if len(sys.argv) != 4:
        exit(HELP_TEXT)
    (mode, source, target) = sys.argv[1:]
    mode = mode.upper()

    # validate target path
    if os.path.exists(target):
        exit("Error: target file already exists.")

    # encode or decode file
    try:
        with open(source, "rb") as sourceHnd, open(target, "wb") as targetHnd:
            if mode == "E":
                for (runLen, runByte) in RLE_encode(sourceHnd):
                    targetHnd.write(bytes((runLen, runByte)))
            elif mode == "D":
                for (runLen, runByte) in RLE_decode(sourceHnd):
                    targetHnd.write(runLen * bytes((runByte,)))
            else:
                exit("Error: invalid mode.")
    except OSError:
        exit("Read/write error.")

if __name__ == "__main__":
    main()
