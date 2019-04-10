import csv
import os
import lzma
import sys
import timeit, functools
import gzip
import ctypes
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dir_path = os.path.dirname(os.path.realpath(__file__))
files_dir = os.path.join(dir_path, "FILES")

if os.name == "posix":
    huffman = ctypes.CDLL("libhuffman.dylib")
    librle = ctypes.CDLL("librle.dylib")
elif os.name == "nt":
    huffman = ctypes.CDLL("huffman.dll")
    librle = ctypes.CDLL("rle.dll")

csv_paths = os.path.join(dir_path, "CSV" + os.path.sep)
columns = ["Алгоритм", "Файл", "Размер до", "Размер после", "Отношение сжатия", "Процент сжатия",
           "Время сжатия", "Время распаковки", "Кол-во запусков функций"]


def wrap_function(lib, name, restype, argtypes):
    func = lib.__getattr__(name)
    func.restype = restype
    func.argtypes = argtypes
    return func


def get_full_path(directory):
    d = os.path.join(dir_path, directory + os.path.sep)
    return d


def get_files(directory):
    d = os.path.join(files_dir, directory + os.path.sep)
    files = [os.path.join(d, f) for f in os.listdir(d) if os.path.isfile(os.path.join(d, f))
             and f != ".DS_Store" and not f.startswith("._")]
    return files


def create_dirs(directory):
    d = os.path.join(files_dir, directory + os.path.sep)
    dirs = ["lzma", "gzip", "huffman", "rle"]
    for d in dirs:
        directory = os.path.join(files_dir, directory + os.path.sep)
        result = os.path.join(directory, d)
        if not os.path.exists(result):
            os.mkdir(result)
    d = os.path.join(dir_path, "CSV" + os.path.sep)
    if not os.path.exists(d):
        os.mkdir(d)


def compress_lzma(filepath):
    subdir = "lzma"
    ext = ".lzma"
    lzma_data = lzma.compress(open(filepath, "rb").read())
    filepath = os.path.join(os.path.dirname(filepath), subdir, os.path.basename(filepath))
    with open(filepath + ext, "wb") as f:
        f.write(lzma_data)
    return filepath + ext


def decompress_lzma(file):
    lzma.decompress(open(file, "rb").read())


def analyze_algorithm(algorithm_name, file, out_csv, compress_func, decompress_func, times):
    t = timeit.Timer((functools.partial(compress_func, file)))
    compressed_file = compress_func(file)
    time_compress = t.timeit(times)
    size_before = os.path.getsize(file)
    size_after = os.path.getsize(compressed_file)
    ratio = round((size_after / size_before), 4)
    percent = 100 - (ratio * 100)

    t2 = timeit.Timer(functools.partial(decompress_func, compressed_file))
    time_decompress = t2.timeit(times)
    #decompress_func(compressed_file)
    # remove compressed files
    os.remove(compressed_file)

    return [algorithm_name, os.path.basename(file), size_before, size_after, ratio, percent, time_compress/times,
            time_decompress/times, times]


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
    if os.name == "posix":
        func = wrap_function(huffman, "huffman_encode_file", int, [ctypes.c_char_p, ctypes.c_char_p])
    elif os.name == "nt":
        func = wrap_function(huffman, "compress", int, [ctypes.c_char_p, ctypes.c_char_p])
    result = func(file.encode('utf-8'), (filepath + ext).encode('utf-8'))
    return filepath + ext


def decompress_huffman(file):
    file_to = os.path.join(str(Path(file).parent), os.path.basename(file))
    if os.name == "posix":
        func = wrap_function(huffman, "huffman_decode_file", int, [ctypes.c_char_p, ctypes.c_char_p])
    elif os.name == "nt":
        func = wrap_function(huffman, "extract", int, [ctypes.c_char_p, ctypes.c_char_p])
    result = func(file.encode('utf-8'), file_to.encode('utf-8'))
    return file_to


def compress_rle(file):
    subdir = "rle"
    ext = ".rle"
    filepath = os.path.join(os.path.dirname(file), subdir, os.path.basename(file))
    func = wrap_function(librle, "RleEncodeFile", int, [ctypes.c_char_p, ctypes.c_char_p])
    result = func(file.encode('utf-8'), (filepath + ext).encode('utf-8'))
    return (filepath + ext)


def decompress_rle(file):
    file_to = os.path.join(str(Path(file).parent), os.path.basename(file))
    func = wrap_function(librle, "RleDecodeFile", int, [ctypes.c_char_p, ctypes.c_char_p])
    result = func(file.encode('utf-8'), file_to.encode('utf-8'))
    return file_to


def analyze_directory(directory="files", times=1):
    create_dirs(directory)
    csv_file_name = os.path.join(csv_paths, "analyze_" + directory + ".csv")
    with open(csv_file_name, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(["Алгоритм", "Файл", "Размер до", "Размер после", "Отношение сжатия", "Процент сжатия",
                         "Время сжатия", "Время распаковки", "Кол-во запусков функций"])

    with open(csv_file_name, "a", newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        for file in get_files(directory):
            writer.writerow(
                analyze_algorithm("RLE", file, csv_file_name, compress_rle, decompress_rle, times))
            writer.writerow(
                analyze_algorithm("Huffman", file, csv_file_name, compress_huffman, decompress_huffman, times))
            writer.writerow(
                analyze_algorithm("LZMA", file, csv_file_name, compress_lzma, decompress_lzma, times))
            writer.writerow(
                analyze_algorithm("DEFLATE", file, csv_file_name, compress_gzip, decompress_gzip, times))

    return csv_file_name


def analyze_average_directory(directory="files", times=1):
    create_dirs(directory)
    csv_file_name = os.path.join(csv_paths, "analyze_average_" + directory + ".csv")
    columns = ["Алгоритм", "Файл", "Размер до", "Размер после", "Отношение сжатия", "Процент сжатия",
               "Время сжатия", "Время распаковки", "Кол-во запусков функций"]
    with open(csv_file_name, 'w', newline='',encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, dialect='excel')
        writer.writerow(columns)

    data1 = []
    data2 = []
    data3 = []
    data4 = []

    for file in get_files(directory):
        data1.append(analyze_algorithm("RLE", file, csv_file_name, compress_rle, decompress_rle, times))
        data2.append(analyze_algorithm("Huffman", file, csv_file_name, compress_huffman, decompress_huffman, times))
        data3.append(analyze_algorithm("LZMA", file, csv_file_name, compress_lzma, decompress_lzma, times))
        data4.append(analyze_algorithm("DEFLATE", file, csv_file_name, compress_gzip, decompress_gzip, times))

    df1 = pd.DataFrame(columns=columns, data=data1)
    df2 = pd.DataFrame(columns=columns, data=data2)
    df3 = pd.DataFrame(columns=columns, data=data3)
    df4 = pd.DataFrame(columns=columns, data=data4)
    count = df1.count()

    average_data = []
    for d in [df1, df2, df3, df4]:
        print(d.to_string())
        size_before = round(d[columns[2]].mean())
        size_after = round(d[columns[3]].mean())
        ratio = round(d[columns[4]].mean(),3)
        percent = round(d[columns[5]].mean(),2)
        time_compress = round(d[columns[6]].mean(),4)
        time_decompress = round(d[columns[7]].mean(),4)
        average_data.append([
            d[columns[0]][0], size_before, size_after, ratio, percent, time_compress, time_decompress,
            d[columns[8]][0]])

    df = pd.DataFrame(columns=columns[0:1] + columns[2:len(columns)], data=average_data)
    df.to_csv(csv_file_name)
    df.name = directory
    print("\nAverage at directory \"{name}\"\n1".format(name=df.name))
    print(df.to_string())
    return df


def create_plot_average(df_list):
    # Compressed percents
    index = [x.name for x in df_list]
    rle = [df[columns[5]][0] for df in df_list]
    huffman = [df[columns[5]][1] for df in df_list]
    lzma = [df[columns[5]][2] for df in df_list]
    deflate = [df[columns[5]][3] for df in df_list]

    df = pd.DataFrame({'RLE': rle, 'Huffman': huffman, "LZMA": lzma, "Deflate": deflate}, index=index)
    ax = df.plot.bar()
    plt.xlabel('Процент сжатия (%)')
    for p in ax.patches:
        ax.annotate(str(round(p.get_height(), 3)), (p.get_x() * 1.005, p.get_height() * 1.005))

    plt.show()

    # Compress and decompress time
    N = len(df_list[0])
    ind = np.arange(N)
    width = 0.5
    groups = ["RLE", "Huffman", "LZMA", "Deflate"]

    for i in range(len(df_list)):
        time_compress = [df[columns[6]] for df in df_list]
        time_decompress = [df[columns[7]] for df in df_list]

        p1 = plt.bar(ind, time_compress[i], width, color="r")
        p2 = plt.bar(ind, time_decompress[i], width, bottom=time_compress[i], color="b")

        plt.ylabel('Time')
        plt.xlabel("Время сжатия/распаковки \"%s\"" % df_list[i].name)
        plt.xticks(ind, groups)
        plt.legend((p1[0], p2[0]), ('compress', 'decompress'))
        plt.show()


def analyze_directories_average(dirs):
    dfs = []
    for dir in dirs:
        if (os.path.exists(os.path.join(files_dir, dir))):
            dfs.append(analyze_average_directory(dir))
    create_plot_average(dfs)


def analyze_directories(dirs):
    dfs = []
    for dir in dirs:
        if os.path.exists(os.path.join(files_dir, dir)):
            dfs.append(analyze_directory(dir))
    # create_plot_average(dfs)


def main(argv):
    if (len(argv) == 1):
        print("Введите режим и директории")
    else:
        if (argv[1].lower() == "average"):
            dirs = argv[2:]
            analyze_directories_average(dirs)
        else:
            dirs = argv[1:]
            analyze_directories(dirs)


if __name__ == '__main__':
    main(sys.argv)
