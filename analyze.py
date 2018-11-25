import csv
import os
import lzma
import timeit, functools
import gzip
import ctypes
import rle
from ctypes.util import find_library


dir_path = os.path.dirname(os.path.realpath(__file__))
huffman = ctypes.CDLL("libhuffman.dylib")

class FILE(ctypes.Structure):
    pass

FILE_p = ctypes.POINTER(FILE)

libc = find_library("c")
print(libc)
#_stdio = FILE_p.in_dll(libc, 'stdio')

def wrap_function(lib, name, restype,argtypes):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func

def get_full_path(directory):
    d = os.path.join(dir_path, directory + os.path.sep)
    return d

def get_file_chars(file):
    #utf8_text = open(file, 'r+').read()
    #return len(utf8_text)
    pass

def get_files(directory):
    d = os.path.join(dir_path, directory+os.path.sep)
    files = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f)) and f != ".DS_Store"]
    return files

def create_dirs(directory):
    d = os.path.join(dir_path, directory + os.path.sep)
    dirs = ["lzma","gzip","huffman","rle"]
    for d in dirs:
        directory = os.path.join(dir_path, directory + os.path.sep)
        result = os.path.join(directory,d)
        if not os.path.exists(result):
            os.mkdir(result)

def compress_lzma(filepath):
    subdir = "lzma"
    ext = ".lzma"
    lzma_data = lzma.compress(open(filepath, "rb").read())
    filepath = os.path.join(os.path.dirname(filepath) ,subdir,os.path.basename(filepath))
    with open(filepath + ext, "wb") as f:
        f.write(lzma_data)
    return filepath + ext

def decompress_lzma(file):
    lzma.decompress(open(file, "rb").read())

def analyze_algorithm(algorithm_name,file, out_csv, compress_func, decompress_func, times):
    t = timeit.Timer(functools.partial(compress_func,file))
    time_compress = t.timeit(times)
    compressed_file = compress_func(file)


    size_before = os.path.getsize(file)
    size_after = os.path.getsize(compressed_file)
    ratio = round((size_after / size_before),4)
    percent = 100 - (ratio * 100)

    t2 = timeit.Timer(functools.partial(decompress_func, compressed_file))
    time_decompress = t2.timeit(times)
    decompress_func(compressed_file)
    end_decompress = timeit.timeit()
    with open(out_csv, "a", newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow([algorithm_name, os.path.basename(file), size_before, size_after, ratio, percent, time_compress,
                         time_decompress, times])



def write_to_csv():
    pass


def compress_gzip(filepath):
    subdir = "gzip"
    ext = ".gzip"
    data = gzip.compress(open(filepath, "rb").read())
    filepath = os.path.join(os.path.dirname(filepath), subdir, os.path.basename(filepath))
    with open(filepath + ext, "wb") as f:
        f.write(data)
    return filepath + ext

def decompress_gzip(file):
    gzip.decompress(open(file, "rb").read())

def compress_huffman(file):
    subdir = "huffman"
    ext = ".huffman"
    filepath = os.path.join(os.path.dirname(file), subdir, os.path.basename(file))
    print(filepath)
    #with open(filepath+ext,"wb") as file:
    func = wrap_function(huffman,"huffman_encode_file", int,[FILE,FILE])
    func((bytes(file,encoding="utf-8")),(bytes(filepath + ext,encoding="utf-8")))


    return filepath+ext

def compress_rle(file):
    subdir = "rle"
    ext = ".rle"
    filepath = os.path.join(os.path.dirname(file), subdir, os.path.basename(file))
    compressed = rle.compress(file, filepath+ext)
    return filepath + ext

def decompress_rle(file):
    subdir = "rle"
    ext = ".rle"
    filepath = os.path.join(os.path.dirname(file), os.path.splitext(os.path.basename(file))[0])
    compressed = rle.decompress(file, filepath)
    return filepath

def analyze(times=100):
    directory = "files"
    csv_file_name =  os.path.join(dir_path ,"analyze_"+directory+".csv")
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(["Алгоритм","Файл","Размер до", "Размер после", "Отношение сжатия", "Процент сжатия",
                         "Время сжатия", "Время распаковки","Кол-во запусков функций"])

    for file in get_files(directory):
        #analyze_algorithm("LZMA", file, csv_file_name, compress_lzma, decompress_lzma, times)
        #analyze_algorithm("GZIP", file, csv_file_name, compress_gzip, decompress_gzip, times)
        #analyze_algorithm("RLE", file, csv_file_name, compress_rle, decompress_rle, times)
        compressed_file = compress_huffman(file)
        #print("%s\nbefore:%s after:%s" % (os.path.basename(file), os.path.getsize(file), os.path.getsize(compressed_file)))



def main():
    create_dirs("files")
    analyze()


if __name__ == '__main__':
    main()
